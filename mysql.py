#Establishing connection
import pandas as pd
import pymysql

connection = pymysql.connect(
    host="localhost",
    database="phonepe pulse",
    user="root",
    password="98655",
)
cursor = connection.cursor()

#creating dataframes
df_aggregated_transaction = pd.read_csv(r'pagg_transaction.csv')
df_aggregated_user=pd.read_csv(r'pagg_users.csv')
df_map_transaction=pd.read_csv(r'pmap_transcation.csv')
df_map_user=pd.read_csv(r'pmap_users.csv')
df_top_transaction=pd.read_csv(r'ptop_transcation.csv')
df_top_user=pd.read_csv(r'ptop_users.csv')
print("Readed Successfully")

import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:98655@localhost/phonepe pulse', echo=False)

#inserting dataframes to mysql
df_aggregated_transaction.to_sql('aggregated_transaction', engine, if_exists='replace',index=False,
                                 dtype= {
                                        "State":sqlalchemy.types.VARCHAR(length=225),
                                        "Year":sqlalchemy.types.INT,
                                        "Quater":sqlalchemy.types.INT,
                                        "Transaction_type":sqlalchemy.types.TEXT,
                                        "Transaction_count ":sqlalchemy.types.INT,
                                        "Transaction_amount ":sqlalchemy.types.FLOAT,})

df_aggregated_user.to_sql('aggregated_user',engine, if_exists='replace',index=False,
                          dtype={"State":sqlalchemy.types.VARCHAR(length=225),
                                 "Year":sqlalchemy.types.INT,
                                 "Quater":sqlalchemy.types.INT,
                                 "brands":sqlalchemy.types.TEXT,
                                 " Count  ":sqlalchemy.types.INT,
                                 "Percentage ":sqlalchemy.types.FLOAT,})

df_map_transaction.to_sql('map_transaction',engine, if_exists='replace',index=False,
                          dtype={"State":sqlalchemy.types.VARCHAR(length=225),
                                 "Year":sqlalchemy.types.INT,
                                 "Quater":sqlalchemy.types.INT,
                                 "District ":sqlalchemy.types.VARCHAR(length=225),
                                 " count  ":sqlalchemy.types.INT,
                                 "amount  ":sqlalchemy.types.FLOAT,})

df_map_user.to_sql('map_user', engine, if_exists='replace',index=False,
                  dtype={"State":sqlalchemy.types.VARCHAR(length=225),
                         "Year":sqlalchemy.types.INT,
                         "Quater":sqlalchemy.types.INT,
                         "District ":sqlalchemy.types.VARCHAR(length=225),
                         "RegisteredUser":sqlalchemy.types.INT,
                                 })

df_top_transaction.to_sql('top_transaction', engine, if_exists='replace',index=False,
                  dtype={"State":sqlalchemy.types.VARCHAR(length=225),
                         "Year":sqlalchemy.types.INT,
                         "Quater":sqlalchemy.types.INT,
                         "District ":sqlalchemy.types.VARCHAR(length=225),
                         "Transaction_count ":sqlalchemy.types.INT,
                         "Transaction_amount ":sqlalchemy.types.FLOAT,})

df_top_user.to_sql('top_user', engine, if_exists='replace',index=False,
                  dtype={"State":sqlalchemy.types.VARCHAR(length=225),
                         "Year":sqlalchemy.types.INT,
                         "Quater":sqlalchemy.types.INT,
                         "District ":sqlalchemy.types.VARCHAR(length=225),
                         "RegisteredUser":sqlalchemy.types.INT,
                                 }) 
print("Loaded Successfully")                               


