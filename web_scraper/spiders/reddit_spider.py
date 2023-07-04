```python
import scrapy
from ..items import Item
from ..utils.pagination_handler import PaginationHandler
from ..utils.dynamic_content_handler import DynamicContentHandler

class RedditSpider(scrapy.Spider):
    name = "RedditSpider"
    start_urls = ['http://www.reddit.com']

    def parse(self, response):
        dynamic_content_handler = DynamicContentHandler()
        pagination_handler = PaginationHandler()

        for post in response.css('div.thing'):
            item = Item()
            item['title'] = post.css('p.title a::text').get()
            item['url'] = post.css('p.title a::attr(href)').get()
            item['upvotes'] = post.css('div.score.unvoted::attr(title)').get()
            yield item

        next_page = pagination_handler.get_next_page(response)
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        dynamic_content = dynamic_content_handler.get_dynamic_content(response)
        if dynamic_content is not None:
            yield from self.parse(dynamic_content)
```