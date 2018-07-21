# -*- coding: utf-8 -*-

import scrapy
from image_scraper.items import ImageScraperItem
from scrapy.spiders import CrawlSpider


class YahooImageSpider(CrawlSpider):

    name = 'yahoo_image'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_id = 0
        self.page_id = 0
        self.image_num_per_page = 20

    def start_requests(self):
        url = ('https://search.yahoo.co.jp/image/search?'
               'p={}&ei=UTF-8&save=0'.format(self.query))
        yield scrapy.Request(url, self.parse, dont_filter=True)

    def parse(self, response):
        self.page_id += 1

        items = ImageScraperItem()
        items['member_id'] = self.member_id
        items['image_ids'] = []
        items['image_urls'] = []

        for src in response.css('#gridlist > div'):
            self.image_id += 1

            url = src.css('div > p > a::attr(href)').extract_first()
            items['image_ids'].append(self.image_id)
            items['image_urls'].append(url)

        yield items

        _next_page = ('https://search.yahoo.co.jp/image/search?fr=top_ga1_sa&'
                      'p={query}&ei=UTF-8&b={start_image}')
        next_page = _next_page.format(
            query=self.query,
            start_image=self.page_id * self.image_num_per_page + 1
        )
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
