# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ImagesPipeline(object):
    def process_item(self, item, spider):
        # tmp = item['image_urls']
        # item['image_urls'] = []
        #
        # for i in tmp:
        #     if "?" in i:
        #         item['image_urls'].append(i.split("?")[0])
        #     else:
        #         item['image_urls'].append(i)
        # print("下载图片:",item['image_urls'])
        # return item
        tmp = item['file_urls']
        item['file_urls'] = []

        for i in tmp:
            if "?" in i:
                item['file_urls'].append(i.split("?")[0])
            else:
                item['file_urls'].append(i)
        print("下载图片:", item['file_urls'])
        return item
