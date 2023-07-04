```python
import json

class DataStorage:
    @staticmethod
    def store_data(item, spider_name):
        file_name = f"{spider_name}_data.json"
        with open(file_name, 'a') as file:
            line = json.dumps(dict(item)) + "\n"
            file.write(line)
```