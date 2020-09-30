import scrapy

class Article(scrapy.Item):
    url = scrapy.Field()
    updated = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()

class Tag(scrapy.Item):
    name = scrapy.Field()
