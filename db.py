# import pymysql
import sqlite3

# conn = pymysql.connect(
#     host='sql6.freesqldatabase.com',
#     database='sql6410975',
#     user='sql6410975',
#     password='8bs3p7gjrX',
#     charset='utf8mb4',
#     cursorclass=pymysql.cursors.DictCursor    
# )
conn = sqlite3.connect("products.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE product(
    id integer PRIMARY KEY,
    Name text NOT NULL,
    Description text NOT NULL,
    Price double NOT NULL,
    PictureUrl text NOT NULL
    
) """
cursor.execute(sql_query)
# conn.close()