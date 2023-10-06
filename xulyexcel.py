# tạo 1 sheet mới với cột là date và các user ID sau đó dùng code này để ra được 1 file mới chứa date và từng user id

import pandas as pd

# Đường dẫn đến file Excel của bạn
#file_path = r"C:\Users\Admin\PycharmProjects\decrypt_data\use_08_10_2023_tech.xlsx"

file_path = r"C:\Users\Admin\PycharmProjects\decrypt_data\use_08_10_2023_take.xlsx"

# Đọc dữ liệu từ file Excel vào DataFrame
df = pd.read_excel(file_path,sheet_name="Sheet3")

# Tạo một DataFrame mới để chứa dữ liệu sau khi tách user ID
new_df = pd.DataFrame(columns=['date', 'userIds'])

# Duyệt qua từng hàng trong DataFrame gốc
for _, row in df.iterrows():
	date = row['date']
	user_ids = row['userIds'].split(',')  # Tách các user ID thành một list

	# Tạo một hàng mới cho mỗi user ID và thêm vào DataFrame mới
	for user_id in user_ids:
		new_row = {'date': date, 'userIds': user_id.strip()}  # Xóa khoảng trắng thừa
		new_df = pd.concat([new_df, pd.DataFrame.from_records([new_row], columns=['date', 'userIds'])],ignore_index=True)

# Ghi DataFrame mới vào file Excel
new_file_path = '12-10_take.xlsx'
new_df.to_excel(new_file_path, index=False)
