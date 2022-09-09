from os import dup
import pandas as pd 

students = pd.read_excel('./TestExcel/output009.xlsx')

row_sum = students[['Firstyear','Lastyear']].sum(axis=1)
students['TotalSales'] = row_sum
col_sum = students[['Firstyear','Lastyear','TotalSales']].sum()
col_sum['Field'] = 'Summary'
students = students.append(col_sum,ignore_index=True)
print(students)
print('\n')

# 取出那些重复的数据
dupe = students.duplicated(subset='Field')
print(dupe.any())
print(dupe.count())
print(dupe[dupe]) #自己和True比较
dupe = dupe[dupe==True]
print(f'dupe的索引:{dupe.index}\n')
print(f'{students.iloc[dupe.index]}\n') #取出那些数据

# 消除重复数据，基于哪些列 subset=['Field',Firstyear'] keep='first'/'last'保留开始还是后面的
students.drop_duplicates(subset='Field',inplace=True,keep='first')
print(students)