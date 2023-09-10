from fastapi import FastAPI
import mysql.connector

app = FastAPI()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="laravel-react-api"
)

#rutas 
@app.get('/')
def index():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT name, email FROM users")
    result = mycursor.fetchall()
    return {'data':result, 'hola':'hola'}