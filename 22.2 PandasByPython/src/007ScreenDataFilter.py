import pandas as pd


def lastPrice_32_to_42(a):
    return a >= 32 and a < 42


def finalPrice_657_to_2000(a):
    return 657 <= a < 2000


books = pd.read_excel('./TestExcel/output007.xlsx', index_col='ID')
# 这边loc定位到某列，按照apply里面的函数关系来进行筛选
# books = books.loc[books['LastPrice'].apply(lastPrice_32_to_42)].loc[books['FinalPrice'].apply(finalPrice_657_to_2000)]
# 可以直接.列名来修改
books = books.loc[books.LastPrice.apply(lastPrice_32_to_42)].loc[books.FinalPrice.apply(finalPrice_657_to_2000)]
books.sort_values(by=['Worthly', 'FinalPrice'], inplace=True, ascending=[True, False])
print(books)
