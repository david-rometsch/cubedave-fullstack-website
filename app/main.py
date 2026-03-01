# main.py
import json
import os
from contextlib import contextmanager

# fastapi imports
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # included in fastapi.
from fastapi.templating import Jinja2Templates

# sqlalchemy imports
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# from typing import Optional

app = FastAPI()

# ==== load dependencies ====
templates = Jinja2Templates(directory="templates")

# ── CORS ────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # z. B. React/Vite
        "http://127.0.0.1:3000",
        "http://localhost:5173",  # Vite default
        "http://127.0.0.1:5173",
        "http://localhost:*",  # wenn du verschiedene Ports testest
        "*",  # ← oder einfach alles erlauben (nur dev!)
    ],
    allow_credentials=True,  # falls du später Cookies brauchst
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS, ...
    allow_headers=["*"],
)

# ==== start db and orm ====#
# avoid confilcts with pre-existing table
if os.path.exists("instance/database.db"):
    os.remove("instance/database.db")

# create engine
engine = create_engine("sqlite:///database.db")
Base = declarative_base()


# Product model
class Product(Base):
    __tablename__ = "product"
    id = Column(String(100), primary_key=True)
    name = Column(String(100))
    size = Column(String(100))
    brand = Column(String(100), nullable=False)
    magnetic = Column(Boolean, nullable=False)
    category = Column(String(100), nullable=False)
    # added {'name': 'YJ MGC 4x4', 'size': '4x4', 'brand': 'YJ', 'magnetic': True, 'category': '4x4'}
    # price = Column(Float())
    # img = Column(String(100), nullable=False)  # will be an existing file path later!

    """@classmethod
    def create(cls, name, image):
        return cls(name, image)"""

    @classmethod
    def read_all(cls, session) -> list[type]:
        """Return list of all instances or []"""
        return session.query(cls).all()

    # def __repr__(self):
    #     return f"id: {self.id}, name: {self.name} image-name: {self.img}"


# sapledata:k
# "name": "DAVID 12 MagLev",
# "size": "3x3",
# "brand": "GAN",
# "magnetic": true,
# "category": "3x3"


# pydantic-interface
class ProductSchema(BaseModel):
    id: str
    name: str
    size: str
    brand: str
    magnetic: bool
    category: str

    class Config:
        from_attributes = True  # only allows SQLAlchemy-Objekte


# create Session-object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# yield session using context manager
@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


# create tables
Base.metadata.create_all(engine)


# load frum json
def load_json_cubes():
    with open("./static/cubes.json", "r", encoding="utf-8") as f:
        dict_of_cubes = json.load(f)
    # print("loc: ", dict_of_cubes)
    return dict_of_cubes


# seed cubes
seed_cubes = load_json_cubes()
with get_session() as session:
    if session.query(Product).count() == 0:
        for s_cube in seed_cubes["cubes"]:
            cube = Product(**s_cube)
            session.add(cube)
            print("added", cube)


# ==== routes ====
# template
# @app.get("/")
# async def home(request: Request):
#     return templates.TemplateResponse(
#         "index.html",  # Name der Datei in templates/
#         {
#             "request": request,  # Muss immer übergeben werden!
#             "title": "Meine coole Seite",
#             "message": "Hello david from Template!",
#         },
#     )
#


# ==== API ====
@app.get("/api/all_cubes", response_model=list[ProductSchema])
async def load_cubes():
    with get_session() as session:
        products = Product.read_all(session)
        return [ProductSchema.model_validate(p) for p in products]


# ==== static files ====# ganz am schluss nach allen routes !!!
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="static")
