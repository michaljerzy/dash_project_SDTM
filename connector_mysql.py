# import necessary packages
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# establish connection with the database
engine = create_engine("mysql+pymysql://cezary:Pass123123@localhost/test?charset=utf8mb4")
dbConnection = engine.connect()

# connect with pandas
data.to_sql('loan_data', engine, if_exists='replace')

oil_production = pd.read_sql("select * from oil_production",dbConnection)

print(oil_production)