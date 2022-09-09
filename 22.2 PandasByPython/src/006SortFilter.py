import pandas as pd

books = pd.read_excel('./TestExcel/output006.xlsx', dtype={'ID': str, 'Name': str}, index_col='ID')
# inplace=True是为了不生产新的DF
# 按照价格排序 ascending默认为True升序排列
# books.sort_values(by='FinalPrice', inplace=True, ascending=False)
# 先按照Worthly排序，再按照FinalPrice排序
books.sort_values(by=['Worthly', 'FinalPrice'], inplace=True, ascending=[True,False])
print(books)
