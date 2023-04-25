import pandas as pd

# Đọc dữ liệu vào DataFrame
df = pd.read_excel(r'C:\Users\MINH QUY\Downloads\Dataset\Dataset\Temperature.xls')

# Tạo bảng phân tổ thống kê
table = pd.crosstab(index=df['Temperature'], columns='count')

# In ra bảng phân tổ thống kê
print(table)
