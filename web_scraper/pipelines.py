```python
import json
from scrapy.exceptions import DropItem
from .utils.data_storage import DataStorage

class WebScraperPipeline:
    def __init__(self):
        self.ids_seen = set()
        self.data_storage = DataStorage()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            self.data_storage.store_in_json(item)
            return item
```