```python
import scrapy

class PaginationHandler:
    @staticmethod
    def get_next_page(response):
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            return scrapy.Request(url=next_page, callback=self.parse)
        return None
```