import pandas as pd
import numpy as np

pd.options.display.max_columns = 777
orders = pd.read_excel('./TestExcel/output017.xlsx')
orders['Year'] = pd.DatetimeIndex(orders.Date).year
print(orders)

piovot_table1=orders.pivot_table(index='Category',columns='Year',values='Total',aggfunc=np.sum)
print(piovot_table1)

groups = orders.groupby(['Category','Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
piovot_table2 = pd.DataFrame({'Sum':s,'Count':c})
print(piovot_table2)