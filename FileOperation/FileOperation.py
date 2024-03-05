import pandas as pd
import docx2txt


class FileOperation:
    def read_csv(self, file_path):
        data = pd.read_csv(file_path)
        # המרת עמודת התאריך לפורמט תאריך
        data['Date'] = pd.to_datetime(data['Date'])
        return data

    def save_to_excel(self, data, file_name: str):
        """save data in an Excel file"""
        pd.DataFrame(data).to_csv(file_name, index=False)
        print(f"Data saved to {file_name} successfully.")

    def read_docx(self, file_path):
        text = docx2txt.process(file_path)
        return text

    def convert_date_format(self, file_path):
        """convert date format while reading from file"""
        date_columns = ['Date']

        def parse_cube_date(x):
            return pd.to_datetime(x, format='%d.%m.%Y')

        data = pd.read_csv(file_path, parse_dates=date_columns, converters={'Date': parse_cube_date})

        return data


class FileOperationMain:
    file_path = "C:\\Users\\user1\\Documents\\תיקיית תיכנות\\שנה ב'\\phyton\\project_YafeNof\\Files\\YafeNof.csv"
    # 1
    print("-----1-----")
    file = FileOperation()
    data = file.read_csv(file_path)
    print(data)
    # 2
    print("-----2-----")
    file.save_to_excel(data, "newFile.csv")
    data_to_write = file.read_csv("newFile.csv")
    print(data_to_write)
    # task 7

