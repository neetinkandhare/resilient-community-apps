# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
import os
import tempfile
from docx import Document
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import xlrd
import six


class IOCParserHelper(object):
    def __init__(self):
        # Resilient Rest Api calls url's
        self.ARTIFACT_META_DATA_URL = "/incidents/{0}/artifacts/{1}"
        self.ARTIFACT_DATA_URL = "/incidents/{0}/artifacts/{1}/contents"
        self.ATTACHMENT_META_DATA_URL = "/incidents/{0}/attachments/{1}"
        self.ATTACHMENT_DATA_URL = "/incidents/{0}/attachments/{1}/contents"
        self.TASK_META_DATA_URL = "/tasks/{0}/attachments/{1}"
        self.TASK_DATA_URL = "/tasks/{0}/attachments/{1}/contents"

    @classmethod
    def extract_text_from_bytes_data(cls, filename, file_data_bytes):
        if not file_data_bytes:
            raise ValueError("{0} is an empty file. Can't be processed for IOC's.".format(filename))
        if filename.endswith('.pdf'):
            """
            Converting .pdf file data to plain text format
            """
            file_string_data = IOCParserHelper.extract_text_from_pdf(file_data_bytes)
        elif filename.endswith('.docx'):
            """
            Converting .docx file data to plain text format
            """
            file_string_data = IOCParserHelper.extract_text_from_docx(file_data_bytes)
        elif filename.endswith('.xls') or filename.endswith('.xlsx'):
            """
            Converting .xls/.xlsx file data to plain text format
            """
            file_string_data = IOCParserHelper.extract_text_from_xls_xlsx(file_data_bytes)
        elif filename.split('.')[-1].strip() in ['doc', 'odt', 'ott', 'dot', 'gz', 'zip', 'tar', 'ods']:
            raise ValueError("These attachment/artifact types are not supported for IOC Parsing,"
                             "Please use string based data or files lik: .docx, .txt, .pdf, .xls, .xlsx etc.")
        else:
            file_string_data = file_data_bytes

        if file_string_data:
            if six.PY2:
                # this removes the ascii character and encodes back to string
                if isinstance(file_string_data, str):
                    file_string_data = file_string_data.decode('ascii', 'ignore').encode('ascii')
                else:
                    file_string_data = file_string_data.encode('ascii', 'ignore')
            elif six.PY3:
                try:
                    file_string_data = str(file_string_data)
                except Exception:
                    raise ValueError("Error while converting file :{0} data to string, "
                                     "ioc parsing can't be processed.".format(filename))
        return file_string_data

    @classmethod
    def extract_text_from_pdf(cls, attachment_input):
        """
        Wrapper to convert bytes data in into PDF file and extracting the text data from .pdf file
        :param attachment_input:  attachment Bytes data from resilient api call
        :return:  Text Data
        """
        resource_manager = PDFResourceManager()
        # To Handle unicode conversion in python 2 and python 3
        if six.PY2:
            fake_file_handle = io.BytesIO()
        else:
            fake_file_handle = io.StringIO()

        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        extracted_input = u""

        with tempfile.NamedTemporaryFile(mode="w+b", delete=True) as temp_pdf_file:
            try:
                # Write and close temp file
                temp_pdf_file.write(attachment_input)

                # Reading the Data from Created Temp File
                for page in PDFPage.get_pages(temp_pdf_file, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)

                extracted_input = fake_file_handle.getvalue()
            except Exception as error_msg:
                raise ValueError("Failed Convert .pdf files data to string format. Error: {0}".format(error_msg))
            finally:
                # close open handles
                converter.close()
                fake_file_handle.close()
        return extracted_input

    @classmethod
    def extract_text_from_docx(cls, attachment_input):
        """
        Wrapper to convert bytes data in into .docx file and extracting the text data from .doc/.docx file
        :param attachment_input:
        :return: Text Data
        """
        extracted_input = u""
        with tempfile.NamedTemporaryFile(mode="w+b", delete=True) as temp_doc_file:
            try:
                # Write and close temp file
                temp_doc_file.write(attachment_input)
                read_doc = Document(temp_doc_file)
                for paragraph in read_doc.paragraphs:
                    extracted_input = u"{0} {1}".format(extracted_input, paragraph.text)
            except Exception as error_msg:
                raise ValueError("Failed Convert .docx files data to string format. Error: {0}".format(error_msg))
        return extracted_input

    @classmethod
    def extract_text_from_xls_xlsx(cls, attachment_input):
        """
        Wrapper to convert bytes data in into .xls/.xlsx file and extracting the text data from .xls/.xlsx file
        :param attachment_input:
        :return: Text Data
        """
        extracted_input = ""
        with tempfile.NamedTemporaryFile(mode="w+b", delete=False, suffix='.xlsx') as temp_doc_file:
            # Write and close temp file
            temp_doc_file.write(attachment_input)
        try:
            workbook_object = xlrd.open_workbook(temp_doc_file.name)
            total_sheets = workbook_object.nsheets
            for sheet_index in range(0, total_sheets):
                each_sheet_obj = workbook_object.sheet_by_index(sheet_index)
                total_rows_each_sheet = each_sheet_obj.nrows
                for row_no in range(0, total_rows_each_sheet):
                    row_data_list = each_sheet_obj.row_values(row_no)
                    for data in row_data_list:
                        extracted_input += str(data) + " "
        except Exception as error_msg:
            raise ValueError("Failed Convert .xlsx/.xls files data to string format. Error: {0}".format(error_msg))
        finally:
            os.unlink(temp_doc_file.name)
        return extracted_input

    def _correct_ioc_value(self, kind, value):
        _formatted_value = ''
        if kind == 'uri':
            if value.startswith('https://') or value.startswith('http://'):
                _formatted_value = value
            else:
                _formatted_value = "{0}{1}".format('https://', value)
        else:
            _formatted_value = value
        return _formatted_value

    def format_iocs(self, ioc_parser_obj_list):
        """Loop each ioc_obj in ioc_parser_obj_list and get its Kind and Value.
        Map each ioc_obj.kind to a Resilient Artifact Type.
        If the kind is not in our map, default it to a String.
        If the ioc.value is found more than once just increment the count.
        Return a List of Dictionaries with the attributes: artifact_type, artifact_value and count
        """

        return_list = []

        ioc_kind_to_artifact_type_map = {
            'uri': 'URL',
            'IP': 'IP Address',
            'md5': 'Malware MD5 Hash',
            'sha1': 'Malware SHA-1 Hash',
            'sha256': 'Malware SHA-256 Hash',
            'CVE': 'Threat CVE ID',
            'email': 'Email Body',
            'filename': 'File Name',
            'string': 'String'
        }

        for ioc_obj in ioc_parser_obj_list:

            ioc_value = self._correct_ioc_value(ioc_obj.kind, ioc_obj.value)

            formatted_ioc_obj = next((ioc
                                     for ioc
                                     in return_list
                                     if ioc.get("artifact_value", None) == ioc_value), None)

            if formatted_ioc_obj is not None:
                formatted_ioc_obj["count"] = formatted_ioc_obj.get("count") + 1

            else:
                return_list.append({
                    "artifact_type": ioc_kind_to_artifact_type_map.get(ioc_obj.kind, "string"),
                    "artifact_value": ioc_value,
                    "count": 1
                })

        return return_list
