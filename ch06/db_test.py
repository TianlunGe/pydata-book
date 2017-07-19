import sqlalchemy
import pandas as pd

en = sqlalchemy.create_engine('mysql+mysqldb://root:root@localhost/fitness')
conn = en.connect()
print(conn)
print(pd.read_sql('classes', conn))
