from flask import Flask, request, jsonify
import json
# import pymysql
import sqlite3

app = Flask(__name__)

def db_connection():
  conn = None
  try:
    # conn = pymysql.connect( 
    # host='sql6.freesqldatabase.com',
    # database='sql6410975',
    # user='sql6410975',
    # password='8bs3p7gjrX',
    # charset='utf8mb4',
    # cursorclass=pymysql.cursors.DictCursor)
    conn =sqlite3.connect('products.sqlite')  
    # cursor = conn.cursor()
  except sqlite3.error as e:
    print(e)
  return conn

@app.route("/")
def welcome():
  return "<h1> WELCOME TO THE PRODUCT MANAGEMENT REST API CRUD OP POC"

@app.route('/products', methods=['GET', 'POST']) 
def products():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
      cursor =  conn.execute("SELECT * FROM product")
      # products = [
      #   dict(id=row['id'], Name=row['Name'], Description=row['Description'], Price=row['Price'], PictureUrl=row['PictureUrl'])
      #   for row in cursor.fetchall()
      # ]
      products = [
        dict(id=row[0], Name=row[1], Description=row[2], Price=row[3], PictureUrl=row[4])
        for row in cursor.fetchall()
      ]
      if products is not None:
        return jsonify(products)        

    if request.method == 'POST':
        new_name = request.form['Name']
        new_desc = request.form['Description']
        new_price = request.form['Price']
        new_pic = request.form['PictureUrl']
        
        sql = """INSERT INTO product(Name, Description, Price, PictureUrl) VALUES(?, ?, ?, ?) """        
        cursor = cursor.execute(sql, (new_name, new_desc, new_price, new_pic))
        conn.commit()
        return f"Product with the id: {cursor.lastrowid} created successfully", 201

@app.route('/product/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_product(id):

  conn = db_connection()
  cursor = conn.cursor()
  product=None
  if request.method == 'GET':
    cursor.execute("SELECT * FROM product WHERE id=?", (id,))
    rows = cursor.fetchall()
    for r in rows:
      product = r
    if product is not None:
      return jsonify(product), 200
    else:
      return "Something wrong", 404
    
  
  if request.method == 'PUT':
    sql = """UPDATE product
            SET Name=?, 
                Description=?,
                Price=?,
                PictureUrl=?
            WHERE id=? """

    Name = request.form['Name']
    Description= request.form['Description']
    Price = request.form['Price']
    PictureUrl = request.form['PictureUrl']
    updated_product = {
      "id": id,
      "Name": Name,
      "Description": Description,
      "Price": Price,
      "PictureUrl":PictureUrl, 
    }
    cursor = cursor.execute(sql, (Name, Description, Price, PictureUrl, id))
    conn.commit()
    return jsonify(updated_product)
  
  if request.method == 'DELETE':
    sql = """ DELETE FROM product WHERE id=?"""
    conn.execute(sql, (id,))
    conn.commit()
    return "The product with id: {} has been deleted.".format(id), 200

if __name__ == '__main__':
    app.run(debug= True)