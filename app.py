'''
start app with: uvicorn:app.py --reload  fuer entwickliung immer mit --reload
'''

import os

from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#from typing import  


# reate app (as object "app")
app = FastAPI()

# ==== start db and orm ====#
# avoid confilcts with pre-existing table
if os.path.exists('instance/database.db'):
    os.remove('instance/database.db')

# create engine
engine=create_engine("sqlite:///database.db")
Base=declarative_base()

# Cube model
class Cube (Base):
    id =  Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float())
    img = Column(String(100), nullable=False)     # will be an existing file path later!

    '''@classmethod
    def create(cls, name, image):
        return cls(name, image)'''

    def __repr__(self): 
        return f"id: {self.id}, name: {self.name} image-name: {self.img}"

# create Session-object
Cube: new_cube=Cube(name: 3x3, size:50mm)
new_cube=false


SessionLocal=sessionmaker() # session factory -> session class
session=SessionLocal(bind=engine) # session-object pro context!
# yield session using context manager
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# create tables
Base.metadata.create_all(engine)

# templating
template=Jinja2Templates(directory="templates")


# ==== routes ====# 
#render index-template
@app.get("/")
def index():
    context = {"key":"value"}
    return template.TemplateResponse("index.html", context) 

# API
@app.get("/cubes/")
async def root (Depends(get_db())):
    cube=query(Cube).All()
    return {name: jcube[0].name}
        
    
