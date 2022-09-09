from typing import SupportsRound
import pandas as pd 

students = pd.read_excel('./TestExcel/output014.xlsx',sheet_name='Students',index_col='ID')
scores = pd.read_excel('./TestExcel/output014.xlsx',sheet_name='Scores',index_col='ID')

# students表join scores表 how表示不论是否能查询到数据始终保持students表的数据 以ID列来join
# fillna 用0来填充空值
# 如果左右两边ID列名字不一样 left_on right_on
# table = students.merge(scores,how='left',left_on=students.index, right_on=scores.index).fillna(0)
table = students.join(scores,how='left').fillna(0)
# 将浮点数转为原始的int数据
table.Score = table.Score.astype(int)
print(table)