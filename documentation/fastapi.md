https://fastapi.tiangolo.com/types/
# installation
```
pip install "fastapi[standard]"  # enthält fastapi-cli
```

# run
```
fastapi dev main.py    # Development-Server (auto-reload)
fastapi run main.py    # Production-Server
```
uvicorn server wird damit automatisch gestartet
## ports
```
alles laeuft auf port 8000
```

# documentation
| doc   | route  |     |
| ----- | ------ | --- |
| docs  | /docs  |     |
| redoc | /redoc | c   |

---
# begriffe
| Begriff                  | Erklärung                                                                                                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAPI                  | Standardisierung des .json (in FastAPI automatisch) sichtbar unter:  [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) das schema ist voraussetzung fuer die documentations |
| /docs (Swagger) / /redoc | /docs ist nur ein UI-Tool, das die echten API-Endpoints aufruft. Die **Requests laufen über dieselben Routen** wie alles andere - es gibt keine "parallele" Verarbeitung.                          |
| fastapi cil              | damit wird fastapi gestartet im terminal                                                                                                                                                           |
## terms
class: code - definition - ebene
type: laufzeit - annotation - ebene

die anwedung von type-declaration (in python freiwilllig) hat fuer lsp vorteile. da der typ bekannt ist, wird bei cube. direkt alle attribute vorgeschlagen! 
# typing
## syntax
```python
from typing import Optional

id : int  # id is declaerd from class int
cube : Cubes # same with own classes = type

def process_item(item: int | str):  # severa types
    print(item)
    
def say_hi(name: Optional[str] = None): # possibly none und hat default none!  bzw optional, aber der default muss vorhanden sein, dammit es auch ohne gestartet werden kann: 
	say_hi()
```

## modern syntax
```python
def say_hi(name: str | None):
    print(f"Hey {name}!")  # entspricht optional! einfacher!
```

## class as type
```python 
class Person:

    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
```


## related
[[pydantic.md]]
[[annotated]]

