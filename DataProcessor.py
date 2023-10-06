#in data lấy được ra file excel


import pandas as pd
from DecryptData import decrypt_aes
from DataCrawler import get_data_from_takeprofit_api,get_data_from_techprofit_api

key = '5u8x/A?D(G+KbPeShVmYq3s6v9y$B&E)'


#encrypted_data = get_data_from_techprofit_api()
encrypted_data = get_data_from_takeprofit_api()

decrypted_data = decrypt_aes(encrypted_data, key)
#print(decrypted_data)
result_data = eval(decrypted_data[:-7])

df_new = pd.DataFrame(result_data)


columns_order = ["date", "route", "userIds"]
df_new = df_new[columns_order]

# Ghi dữ liệu mới vào file Excel
df_new.to_excel("use_12_10_2023_take.xlsx", index=False)
#print(df_new)
