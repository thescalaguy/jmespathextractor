# jmespathextractor  

Extract values from deeply-nested JSON using JMESPath expressions.  

## Usage

```python
from jmespathextractor import Extractor

instance = {"user": {"name": "John Doe"}}
ex = Extractor({"user_name": "user.name"})
result = ex.extract(instance=instance)

assert result["user_name"] == "John Doe"
```