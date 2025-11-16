from flask import Flask, render_template

# import my modules
#from ORM import orm, Cube

# reate app (as object "app")
app = Flask(__name__)
#cube = Cube.Query.first()

# configure db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create db
#with app.app_context():
#    db.create_all()
#start db
# Cube.name hardcoded
cubes = [
        {'name': 'icy cube', 'price': '8.95', 'img': 'icy_cube'}, 
        {'name': 'mirror cube', 'price': '15.00', 'img': 'mirror_cube'}, 
        {'name': 'void cube', 'price': '22.95', 'img': 'void_cube'}, 
        
]
# ==== start routing ====#
@app.route("/")
def index_route():
    return render_template('index.html')

@app.route("/shop.html")
def shop_route():     # hardcoded example (later dynamic)
    return render_template("shop.html",cubes = cubes)

# actualize
#@app.route("shop.html/?cubes=1", method=[GET])  # 