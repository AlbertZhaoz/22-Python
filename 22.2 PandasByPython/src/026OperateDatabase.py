import pandas as pd
import numpy as np
import pyodbc as dbc 
# ORM框架 create_engine
import sqlalchemy

books = pd.read_excel('./TestExcel/output019.xlsx')
print(books)

# 此处注意Server={ServerName} ServerName未必是{local}
connection = dbc.connect('Driver={SQL Server};'
                      'Server={DESKTOP-07OJ9VD};'
                      'Database=AlbertBook;'
                      'Trusted_Connection=yes;')

query = 'Select Title from T_Books'
df1 = pd.read_sql_query(query,connection)
print(df1)