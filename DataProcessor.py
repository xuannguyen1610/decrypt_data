import pandas as pd
from DecryptData import decrypt_aes

key = '5u8x/A?D(G+KbPeShVmYq3s6v9y$B&E)'

# Read encrypted data from the text file
with open(r"C:\Users\Admin\PycharmProjects\decrypt_data\encrypted_data.txt", "r") as file:
    encrypted_data = file.read()

decrypted_data = decrypt_aes(encrypted_data, key)
#print(decrypted_data)
result_data = eval(decrypted_data[:-4])

df_new = pd.DataFrame(result_data)


columns_order = ["date", "route", "userIds"]
df_new = df_new[columns_order]

# Ghi dữ liệu mới vào file Excel
df_new.to_excel("use_03_10_2023_take.xlsx", index=False)
