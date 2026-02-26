[[fastapi]]

## example
```python
from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
```

pythn macht nichts mit "thyis is just metadata" es ist eine moeglichkeit metadata mitzugeben. 