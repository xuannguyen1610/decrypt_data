import pandas as pd
from DecryptData import decrypt_aes
from Data import get_data_from_api

encrypted_data = get_data_from_api()
key = '5u8x/A?D(G+KbPeShVmYq3s6v9y$B&E)'

decrypted_data = decrypt_aes(encrypted_data, key)

result_data = eval(decrypted_data[:-1])

df_new = pd.DataFrame(result_data)


columns_order = ["date", "route", "userIds"]
df_new = df_new[columns_order]


# Ghi dữ liệu mới vào file Excel
df_new.to_excel("use_28_06_2023_2.xlsx", index=False)