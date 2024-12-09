import pandas as pd
from sqlalchemy import create_engine

#connect to server
conn_string = 'postgresql://postgres:Onajourney123#@localhost/museum'
db = create_engine(conn_string)
conn = db.connect()

#import csv dataset into database 'museum' using loop

files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv(f'C:/Users/aniwa/OneDrive/Desktop/New World/Data Analyst Portfolio/Museum Painting Analysis in SQL/Museum_Dataset/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)
