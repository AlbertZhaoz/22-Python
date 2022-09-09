import pandas as pd
import numpy as np


students = pd.read_excel('./TestExcel/output014.xlsx',sheet_name='Students')
scores = pd.read_excel('./TestExcel/output014.xlsx',sheet_name='Scores')

# 列横向拼接
list_total = pd.concat([students,scores],axis=1).reset_index(drop=True)
print(list_total)

# 行追加第二种写法
list_total2 = pd.concat([students,scores],ignore_index=True).reset_index(drop=True)
print(list_total2)

# 将ID相同Join进来
list_total3 = students.merge(scores,how='left',on=['ID','ID'])

# 追加一列：
list_total3['Age'] = 25
list_total3['RealAge'] = np.arange(0,len(list_total3))
print(f'Total3:\n{list_total3}\n')
print(np.arange(0,len(list_total3)))

# 删除列
list_total3.drop(columns=['Age','RealAge'],inplace=True)
print(f'DropTotal3:\n{list_total3}\n')

# 插入列
list_total3.insert(1,column='Foo',value=26)
print(f'DropTotal3:\n{list_total3}\n')

# 列名大写
list_total3.rename(columns={'Foo':'FOO'},inplace=True)
print(f'Upper:\n{list_total3}\n')

# 删除空行
list_total3.dropna(inplace=True)
print(f'Dropnan:\n{list_total3}\n')