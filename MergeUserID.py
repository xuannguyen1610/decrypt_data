import pandas as pd

df = pd.read_excel(r"C:\Users\Admin\PycharmProjects\decrypt_data\use_t9_2023_take.xlsx",sheet_name="2023-09-30")

#df = pd.read_excel(r"C:\Users\Admin\PycharmProjects\decrypt_data\use_t9_2023_tech.xlsx",sheet_name="2023-09-30")

unique_ids = set()

for index, row in df.iterrows():
    unique_ids.add(row['userIds'])

merged_ids = ', '.join(str(id) for id in unique_ids)
print(merged_ids)

