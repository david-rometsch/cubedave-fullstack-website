from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# import my modules
from models import Cube
from db import db

# reate app (as object "app")
app = Flask(__name__)

# avoid confilcts with pre-existing table
if os.path.exists('instance/database.db'):
    os.remove('instance/database.db')

# configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # instance/.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# bind db to app
db.init_app(app)

# create db
with app.app_context():
    # generate database
    db.create_all()

    # load demo-data
    db.session.add_all([
        Cube(name= "icy cube", price= 8.95, img= "icy_cube"),
        Cube(name= "mirror cube", price= 15.00, img= "mirror_cube"),
        Cube(name= "void cube", price= 22.95, img= "void_cube")
    ])
    db.session.commit()
    print("Cubes commited to db")

# ==== start routing ====#
@app.route("/")
def index_route():
    return render_template('index.html')

@app.route("/shop.html")
def shop_route():     # hardcoded example (later dynamic)
    cubes =  Cube.query.all()
    
    return render_template("shop.html",cubes = cubes)

# actualize
#@app.route("shop.html/?cubes=1", method=[GET])  # 