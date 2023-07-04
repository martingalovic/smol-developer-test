```python
import scrapy

class RedditItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    subreddit = scrapy.Field()
    upvotes = scrapy.Field()
    comments = scrapy.Field()

class OnlyFansItem(scrapy.Item):
    username = scrapy.Field()
    post_url = scrapy.Field()
    post_content = scrapy.Field()
    likes = scrapy.Field()
    comments = scrapy.Field()
```