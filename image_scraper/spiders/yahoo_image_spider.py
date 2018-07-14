# -*- coding: utf-8 -*-

import scrapy
from image_scraper.items import ImageScraperItem


DOWNLOAD_LIMIT = 1000


class YahooImageSpider(scrapy.Spider):

    name = 'yahoo_image'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_id = 0

    def start_requests(self):
        url = ('https://search.yahoo.co.jp/image/search?'
               'p={}&ei=UTF-8&save=0'.format(self.query))
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        items = ImageScraperItem()
        items['query'] = self.query
        items['image_urls'] = []

        for src in response.css('#gridlist > div'):
            self.image_id += 1

            url = src.css('div > p > a > img::attr(src)').extract_first()
            items['image_urls'].append(url)

            if self.image_id >= DOWNLOAD_LIMIT:
                return items
            else:
                yield items

        css_next_page = '#Sp1 > p > span.m > a::attr(href)'
        next_page = response.css(css_next_page).extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

