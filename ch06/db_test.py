import sqlalchemy

en = sqlalchemy.create_engine('mysql+mysqldb://root:root@localhost/fitness')
conn = en.connect()
print(conn)

