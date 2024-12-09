import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:Onajourney123#@localhost/museum'
db = create_engine(conn_string)
conn = db.connect()