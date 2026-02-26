---
id: pydantic
aliases: []
tags: []
---
## von tiangolo
[[fastapi]]



#pydantic #fastapi #sqlalchemy #typen

```schema.py
from pydantic import BaseModel

Class StudentOut(BaseModel) # ensures, that only the named fields with the right types get used.
	id: int
	name: str
```

```main.py
@app.get("/api/students", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)) -> list[StudentOut]:
    students = db.scalars(select(Student).order_by(Student.name)).all()
    return [StudentOut.model_validate(s) for s in students]
```

```student.py
from sqlalcehmy import Base

class Student(Base)
	id: Column(String) 
	name: Column(String)
	ahv: Column(String) # never put in json (if .model_validate), because not in StudentOut
```