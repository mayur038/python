import pandas as pd
from sqlalchemy import create_engine
import pymysql

strdb = "mysql+pymysql://'root':''@'localhost'/'ssip'"
db_connection = create_engine(strdb)

q1 = pd.read_sql('select * from users',con=db_connection)