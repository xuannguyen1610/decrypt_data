# chia mỗi ngày đăng nhập ra 1 sheet, với mỗi ngày sẽ lấy được các user sử dụng nhưng chưa lấy được unique

import pandas as pd

df = pd.read_excel(r"C:\Users\Admin\PycharmProjects\decrypt_data\use_08_10_2023_tech.xlsx",sheet_name="2023-10-12")

#df = pd.read_excel(r"C:\Users\Admin\PycharmProjects\decrypt_data\use_08_10_2023_take.xlsx",sheet_name="2023-10-12")

unique_ids = set()

for index, row in df.iterrows():
    unique_ids.add(row['userIds'])

merged_ids = ', '.join(str(id) for id in unique_ids)
print(merged_ids)

