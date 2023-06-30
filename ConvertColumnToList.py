import pandas as pd

# Đường dẫn đến tệp Excel
file_path = r"C:\Users\Admin\PycharmProjects\decrypt_data\so_ngay_dn.xlsx"

# Đọc dữ liệu từ tệp Excel vào DataFrame
df = pd.read_excel(file_path)

# Lấy giá trị của cột 'ColumnName' và chuyển đổi thành danh sách
column_data = df['Số Unique'].tolist()

# In danh sách giá trị của cột
print(column_data)
