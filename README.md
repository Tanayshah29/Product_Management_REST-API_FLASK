# Product Management REST API using FLASK

1) Product Management REST API was created using Flask that performs CRUD operations on Products. 
2) Product's data is stored in Sqlite database. 
3) Tested the APIs in Postman.
4) Deployment is done on Heroku.

##Steps to be followed to run the project

1) Create a virtual environment (myEnv) using these commands:

    a)pip install virtualenv
    
    b)virtualenv myEnv -p python3
    
    c).\\myEnv\\Scripts\\activate
    
    After c) you must see -> (myEnv) YourFolderPath> 
    
    d)pip install flask
    
    Optional-> pip freeze command to see stalled packages

2) To run the app.py/db.py file -> python app.py / python db.py

   After running the db.py -> products.sqlite file will be created
   
   After running the app.py -> Running on http://127.0.0.1:5000/
   
3) Test APIs on POSTMAN through localhost:5000/
  
  a) GET localhost:5000/products -> To get list of all the products from the database in JSON format
  
  b) POST localhost:5000/products -> INSERTS the Data specified in the Body into the database
  
  c) GET localhost:5000/product/1 -> To get a single product from the database in JSON format
  
  d) PUT localhost:5000/product/1 -> UPDATE the product with id=1 in the database
  e) DELETE localhost:5000/product/1 -> DELETE a product from the database
  
4)You can see the records in Sqlite Database in VS code by installing the sqlite extension and then press Ctrl+Shift+P and type Open Database and choose the products.sqlite file. In the Sqlite explorer you can see the records.

5)Deployment to Heroku-
  
  a)pip install gunicorn
  
  b)Create Procfile
  
  c)pip freeze > requirements.txt
  
  d)Login to your Heroku account and create new app product-management-api-poc(anyname). Also download Heroku CLI.
  
  e)Terminal-> git init .
  
            -> git add --all
            
            -> git commit -m "initial commit"
            
            -> heroku login
            
            -> heroku git:remote -a product-management-api-poc
            
            -> git push heroku master
            
  f)Now the app can directly run at https://product-management-api-poc.herokuapp.com/
