import scrapy

from pep_parse.items import PepParseItem
from urllib.parse import urljoin


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        """Парсер ссылок на страницы Pep."""

        all_table = response.css('section[id=numerical-index]')
        tables = all_table.css('tr')

        for i, table in enumerate(tables):
            if i == 0:
                continue
            if i == 10:
                break
            row = table.css('td')
            pep_link = urljoin(
                PepSpider.start_urls[0], row.css('a::attr(href)').get()
            )
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсер страницы Pep."""

        h1 = response.css('h1.page-title::text').get()

        item = PepParseItem()
        item['Номер'] = int(h1[:h1.find(' –')].replace('PEP ', ''))
        item['Название'] = h1[h1.find(' –') + 3:]
        item['Статус'] = response.css('dt:contains("Status") + dd::text').get()

        yield item
