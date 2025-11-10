from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cubes ():
    id: Mapped[id] = mapped_column(primary_key=True)
    name: Mapped[str] 
    image: Mapped[str]      # will be an existing file path later!

