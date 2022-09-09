import pandas as pd

# DataFrame-->Worksheet
# 初始化数据
df = pd.DataFrame({'ID': [1, 2, 3, 4, 5, 6], 'Name': ['Tim', 'Victor', 'Nick', 'Timthony', 'Yangzhongke', 'Zack']})
# 设置ID为索引，而不是默认的ID 0 1 2
df = df.set_index('ID')
print(df.columns)
print(df)
excelPath = './TestExcel/output.xlsx'  # 使用相对路径
df.to_excel(excelPath)
print('Create excel successfully!')
