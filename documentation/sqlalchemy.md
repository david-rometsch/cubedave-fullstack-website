---
id: sqlalchemy
aliases: []
tags: []
---

# engine

from sqlalchemy import create_engine

engine=create_engine("sqlite:///rel/path/to/mydb.db")

## models

from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base
class Model(Base)
...

# create tables

Base.metadata.create_all(engine)

# session

from sqlalchemy.orm import session_maker

Session=session_maker() # session factory -> session class  
session=Session(bind=engine) # session-object pro context! - session.

new line in sqlalchemy
