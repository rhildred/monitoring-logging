from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json
Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("postgresql://lcbo:Secret5555@localhost/lcbo")

# reflect the tables
Base.prepare(autoload_with=engine)

# mapped classes are now created with names by default
# matching that of the table name.
Product = Base.classes.products

session = Session(engine)

u1 = session.query(Product).first()
print(u1.__dict__)
