# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider

from suning.items import SuningItem


class GoodsSpider(Spider):
    name = 'goods'
    allowed_domains = ['suning.com','suning.cn']
    start_urls = ['https://list.suning.com/0-346868-0.html']

    def parse_item(self, response):
        i = {}
        print(response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    def parse(self,response):
        i = 1
        while True:

            if i>=100:
                break

            next_url = "https://list.suning.com/0-346868-{}.html".format(i)
            node_list = response.xpath('//*[@id="filter-results"]/ul/li')

            for node in node_list:

                item = SuningItem()

                item['url'] = response.url
                item['good_name'] = node.xpath('./div/div/div/div[2]/p[2]/a/text()').extract_first()
                item['good_url'] = "https:" + node.xpath('./div/div/div/div[2]/p[2]/a/@href').extract_first()

                item['timestamp'] = time.time()

                item['soler'] = response.xpath('./div/div/div/div[2]/p[4]/@salesname').extract_first()


                item['soler_url'] = response.xpath('./div/div/div/div[2]/p[4]/a/@href').extract_first()

                item['image_url'] = response.xpath('.//dl/dd[1]/a/img/@src').extract()


                temp = item['good_url'].split('/')

                item['soler_id'] = temp[3]
                item['good_id'] = "%0.18d" %int(temp[4].split('.')[0])

                price_url = "https://ds.suning.cn/ds/generalForTile/{}_-020-2-{}-1--ds0000000007709.jsonp?callback=ds0000000007709".format(item['good_id'],item['soler_id'])

                yield scrapy.Request(price_url,callback=self.parse_price,meta={'item_1':item},dont_filter=True)

            i += 1
            yield scrapy.Request(next_url)


    def parse_price(self,response):

        item = response.meta['item_1']

        # print("-------------------------",type(response.body.decode()))

        item['price'] = response.body.decode().split(',')[2].split(':')[1]

        yield item
