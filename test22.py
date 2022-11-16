import pandas as pd
tables = pd.read_html('https://finance.naver.com/item/coinfo.naver?code=005930')
print(f'Total tables: {len(tables)}')
print(tables)