# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pathlib
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import md5sum


class ImageScraperPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        member_id = item['member_id']
        for img_id, url in zip(item['image_ids'], item['image_urls']):
            meta = {
                'member_id': member_id,
                'image_id': img_id
            }
            yield scrapy.Request(url, meta=meta)

    def image_downloaded(self, response, request, info):
        checksum = None
        for path, image, buf in self.get_images(response, request, info):
            if checksum is None:
                buf.seek(0)
                checksum = md5sum(buf)
            width, height = image.size
            suffix = pathlib.Path(path).suffix
            path = '{member_id:03d}/{image_id:04d}{suffix}'.format(
                member_id=int(request.meta['member_id']),
                image_id=request.meta['image_id'],
                suffix=suffix
            )
            self.store.persist_file(
                path=path,
                buf=buf,
                info=info,
                meta={'width': width, 'height': height}
            )
        return checksum
