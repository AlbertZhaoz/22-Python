import pandas as pd

Students = pd.read_excel('./TestExcel/output015.xlsx')
#  一列数据分割成两列expand=True n=0切出来多少子字符串就保留多少
df = Students.Name.str.split('_',expand=True)
Students['StudentTitle'] = df[0].str.upper()
Students['StudentIndex'] = df[1]
print(Students)