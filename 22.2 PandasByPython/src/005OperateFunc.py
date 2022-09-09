import pandas as pd


def add_2(x):
    return x + 2


books = pd.read_excel('./TestExcel/output005.xlsx', dtype={'ID': str, 'Name': str},index_col='ID')

for i in books.index:
    books['FirstPrice'].at[i] = 20 + i;
    books['LastPrice'].at[i] = 30 + i;
# 列计算无需取出每行，直接列运算即可
books['FinalPrice'] = books['FirstPrice'] * books['LastPrice']
# 自己列加2块钱
books['FinalPrice'] += 2
# 另一种方式追加2块钱，函数
books['FinalPrice'] = books['FinalPrice'].apply(add_2)
# 另一种方式追加2块钱，lambda表达式
books['FinalPrice'] = books['FinalPrice'].apply(lambda x: x + 2)
print(books)
books.to_excel('./TestExcel/output005.xlsx')
