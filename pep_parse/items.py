import scrapy


class PepParseItem(scrapy.Item):
    """Описание Items для парсера Pep."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
