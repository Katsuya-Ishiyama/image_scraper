# -*- coding: utf-8 -*-

import scrapy


class YahooImageSpider(scrapy.Spider):

    name = 'yahoo_image'

    def start_requests(self):
        url = ('https://search.yahoo.co.jp/image/search?'
               'p={}&ei=UTF-8&save=0'.format(self.query))
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        query = self.query
        img_id = 0

        for src in response.css('#gridlist > div'):
            img_id += 1
            yield {
                'id': img_id,
                'query': query,
                'src': src.css('div > p > a > img::attr(src)').extract_first()
            }

