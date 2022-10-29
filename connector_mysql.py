import mysql.connector as connection
import pandas as pd
try:
    mydb = connection.connect(host="localhost", database = 'test',user="cezary", passwd="Pass123123",use_pure=True)
    query = "Select * from oil_production;"
    result_dataFrame = pd.read_sql(query,mydb)
    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))