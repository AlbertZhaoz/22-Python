import pandas as pd

excelPath = './TestExcel/output.xlsx'  # 使用相对路径
# 指定ID为索引列
outExcel = pd.read_excel(excelPath, index_col='ID')
# outExcel = pd.read_excel(excelPath, header=1)  # 从第1行开始作为标题
# 如果excel里面没有header，但是我们知道如何操作？下面两行
# 操作将Name列显示为了SubName
outExcel = pd.read_excel(excelPath, header=None)
outExcel.columns = ['ID', 'SubName']
# 将修改好的数据SubName写到新的文件中
outExcel.set_index('ID', inplace=True)
outExcel.to_excel('./TestExcel/output002.xlsx')
print('Done')
print(outExcel.shape)  # 显示出这个表有几行几列
print(outExcel.columns)  # 显示出所有列名称
print(f'我是文件头两行数据:\n{outExcel.head(2)}')  # 查看前2行
print(f'我是文件尾三行数据:\n{outExcel.tail(3)}')  # 后三行
