from fastapi import FastAPI
#import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from databases import Database

app = FastAPI()
#definicion de db
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/laravel-react-api"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
database = Database(SQLALCHEMY_DATABASE_URL)

#clase Trainer 
class Trainer(Base):
    __tablename__ = "trainers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    last_name = Column(String(255))
    profile_picture_url = Column(String(255))

#clase Specialist 
class Specialist(Base):
    __tablename__ = "specialists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    last_name = Column(String(255))
    profile_picture_url = Column(String(255))


#metodos para acceder al orm 
@app.on_event("startup")
async def startup():
    await database.connect()
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



#rutas 
@app.get('/trainers')
async def get_trainers():
    db = SessionLocal()
    trainers = db.query(Trainer).all()
    return {'trainers': trainers}

@app.get('/specialists')
async def get_specialists():
    db = SessionLocal()
    specialists = db.query(Specialist).all()
    return {'specialists': specialists}