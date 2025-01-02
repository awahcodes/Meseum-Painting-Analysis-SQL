# Museum Paintings Analysis

## Project Overview:
The project provides answers to business queries on Museum paintings using SQL. Datasets comprises structured data in csv files which were used for the EDA.

## Data Sources
The Project dataset was obtained from Kaggle and the business questions were answered using SQL.
The datasets were  in csv files which were imported into PostgreSQL using Python. Libraries used were Pandas and Sqlalchemy.

## Tools
- Python: To import downloaded data into PostgreSQL
- PostgrSQL: Data wrangling and analysis

## Data preparation
- Python
   - Downloaded dataset from Kaggle was read in pandas to get a quick overview.
   - Below sript was written to import the dataset into postgreSQL
   ```Python

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
   ```

## Questions
- Click  to see all [Questions](https://github.com/awahcodes/Meseum-Painting-Analysis-SQL/blob/master/Questions.txt)
 

## Answers
- Click  to see all [Answers](https://github.com/awahcodes/Meseum-Painting-Analysis-SQL/blob/master/Answers.txt) 
