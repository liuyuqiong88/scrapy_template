# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver

from suning.settings import USER_AGENTS


class SpiderTemSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpiderTemDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 随机user_agent类
class RandomUserAgent(object):

    def process_request(self, request, spider):
        # 随机获取一个ua
        ua = random.choice(USER_AGENTS)

        # 设定
        request.headers['User-Agent'] = ua


# selenium　获取数据
class SeleniumMiddleware(object):
    """返回一个htmlresponse"""

    def process_request(self, request, spider):

        url = request.url

        if 'daydata' in url:
            # 构建浏览器对象
            driver = webdriver.Chrome()
            # 加载页面
            driver.get(url)
            # 休眠--等待渲染完毕
            time.sleep(3)
            # 保存渲染之后的源码
            data = driver.page_source
            # 关闭浏览器
            driver.close()

            # 创建响应，并返回给引擎
            res = HtmlResponse(
                url=request.url,
                body=data,
                request=request,
                encoding='utf-8'
            )
            return res



# 苏宁价格
#             0070094507/10242981060
# https://ds.suning.cn/ds/generalForTile/000000010529848583_-020-2-0070211614-1--ds0000000007709.jsonp?callback=ds0000000007709
#https://ds.suning.cn/ds/generalForTile/000000000617557221__2_0070062935,000000000620645117__2_0070162853,000000010321316326__2_0070116240,000000010445627239__2_0070062935,000000010243612509__2_0070100229,000000000607037589_,000000000612917680__2_0070075676,000000000618434109__2_0070162853,000000010524717800_-020-2-0070074640-1--ds0000000009811.jsonp?callback=ds0000000009811
# https://ds.suning.cn/ds/generalForTile/000000010242981060_-020-2-0070094507-1--ds0000000007709.jsonp?callback=ds0000000007709