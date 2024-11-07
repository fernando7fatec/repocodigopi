import pyodbc
import config

drivers = [item for item in pyodbc.drivers()]
print(drivers)
driver = drivers[-1]

# criar um arquivo config.py 
# a NÃO INCLUIR NO GitHub (use .gitignore )
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
SERVER = config.SERVER
DATABASE = config.DATABASE 

sql = "SELECT * FROM ITENSOS WHERE MAQUINA = 23"

connectionString = f'DRIVER={driver};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
cursor.execute(sql)
r = cursor.fetchone()

print(r)
cursor.close()