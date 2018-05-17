# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import json
from scrapy.conf import settings



class MongoPipeline(object):

    def open_spider(self, spider):
        # 从settings文件中读取配置信息
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        db = settings['MONGO_DB']
        col = settings['MONGO_COL']
        # print(host, port,db,col)

        # 创建数据库链接
        self.client = MongoClient(host, int(port))
        # 选择数据库
        self.db = self.client[db]
        # 选择集合
        self.col = self.db[col]

    def process_item(self, item, spider):
        dict_data = dict(item)
        self.col.insert(dict_data)

        return item

    def close_spider(self, spider):
        self.client.close()


class SpiderTemPipeline(object):
    def process_item(self, item, spider):
        return item
