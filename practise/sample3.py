import pandas_oracle.tools as pt
import os
import pandas as pd

query = "SELECT * FROM test"    

conn = pt.open_connection('PANDAS\oracle\config2.yml')   

df_emp = pt.query_to_df(query, conn, 1000000000) 

df_emp.info()
emp_json = df_emp.to_json()
print(emp_json)

with open('emp.json', 'w') as f:
    f.write(emp_json)

