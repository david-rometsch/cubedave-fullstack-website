
from pydantic import BaseModel

# CubeOut gets createt parallel to the model Cube, 
# But it is only an interface and it is not connected yet. it gets connectet at
# routing with @app.get... wiht Cube:
CubeOut(BaseModel):
    id: int
    name: str

    

