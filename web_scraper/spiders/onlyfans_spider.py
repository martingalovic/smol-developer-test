```python
import scrapy
from ..items import Item
from ..utils.pagination_handler import PaginationHandler
from ..utils.dynamic_content_handler import DynamicContentHandler

class OnlyFansSpider(scrapy.Spider):
    name = 'onlyfans'
    allowed_domains = ['onlyfans.com']
    start_urls = ['http://onlyfans.com/']

    def parse(self, response):
        dynamic_content_handler = DynamicContentHandler()
        data = dynamic_content_handler.handle(response)

        for post in data:
            item = Item()
            item['title'] = post['title']
            item['content'] = post['content']
            item['date'] = post['date']
            yield item

        pagination_handler = PaginationHandler()
        next_page = pagination_handler.handle(response)

        if next_page is not None:
            yield response.follow(next_page, self.parse)
```