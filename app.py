from flask import Flask
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from fastapi.encoders import jsonable_encoder
Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("postgresql://lcbo:Secret5555@localhost/lcbo")

# reflect the tables
Base.prepare(autoload_with=engine)

# mapped classes are now created with names by default
# matching that of the table name.
Product = Base.classes.products
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/products/<id>')
def products(id):
    session = Session(engine)
    u1 = session.query(Product).filter(Product.id == id).first()
    return jsonable_encoder(u1), 200
