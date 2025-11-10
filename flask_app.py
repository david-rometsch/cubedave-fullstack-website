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
cube_name = 'gan air sm 356'
# ==== start routing ====#
@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/shop.html")
def shop(cube=cube_name):     # hardcoded example (later dynamic)
    return render_template("shop.html",name = cube)