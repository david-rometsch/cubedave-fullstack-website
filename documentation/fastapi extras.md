# Dependent()

 #pydantic
# yield session using context manager
def get_db():
db=SessionLocal()
try:
yield:
    db
finally: 
db. close()

## templating
from fastapi.templates import Jinja2Templates

templates=Jinja2Templates(directory="templates")

regulations
