import sqlite3 as sql
import pandas as pd

con = sql.connect('db.sqlite3')
wb = pd.ExcelFile('PokemonStatus.xlsx')

for sheet in wb.sheet_names:
    df = pd.read_excel('PokemonStatus.xlsx', sheet_name=sheet)
    df.to_sql(sheet, con, index=False, if_exists="replace")

con.commit()
con.close()

# Supporting construction: https://www.alixaprodev.com/2022/04/convert-excel-to-database-in-python.html