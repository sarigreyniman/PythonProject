import unittest
import pandas as pd
from unittest.mock import patch
from FileOperation.FileOperation import FileOperation


class FileOperationTest(unittest.TestCase):

    def setUp(self):
        self.file_operation = FileOperation()

    @patch('pandas.read_csv')
    def test_read_csv(self, mock_read_csv):
        test_data = pd.DataFrame({'Date': ['2024-01-01', '2024-01-02'],
                                  'Value': [1, 2]})
        mock_read_csv.return_value = test_data
        result = self.file_operation.read_csv('test.csv')
        self.assertEqual(result.to_dict(), test_data.to_dict())

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_excel(self, mock_to_csv):
        data = {'Date': ['2024-01-01', '2024-01-02'],
                'Value': [1, 2]}
        file_name = 'test.csv'
        self.file_operation.save_to_excel(data, file_name)
        mock_to_csv.assert_called_once_with(file_name, index=False)

    @patch('docx2txt.process')
    def test_read_docx(self, mock_process):
        mock_process.return_value = "Test text"
        result = self.file_operation.read_docx('test.docx')
        self.assertEqual(result, "Test text")


if __name__ == '__main__':
    unittest.main()
