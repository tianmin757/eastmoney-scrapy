# -*- coding: utf-8 -*-
import scrapy
import pymysql
from eastmoney.items import EastmoneyItem

class EastbasicSpider(scrapy.Spider):
    name = "eastbasic"
    allowed_domains = ["eastmoney.com"]
    #start_urls=['http://quote.eastmoney.com/SZ002543.html',
    #            'http://quote.eastmoney.com/SZ000001.html']
    
    def start_requests(self):
       conn=pymysql.connect(host='localhost',
                     user='root',
                     passwd='root',
                     db='test',
                     charset='utf8')
       sql='select stock_url from test.eastmoney_basic_info'
       cursor=conn.cursor()
       cursor.execute(sql)
       b=cursor.fetchall()
       for url in b:
            string_url=''.join(tuple(url))
            yield scrapy.Request(url=string_url,callback=self.parse)  
       
        
    def parse(self, response):
        
        item=EastmoneyItem()
        item["stock_id"]=response.css("#code::text").extract()
        item["name"]=response.css(".cwzb > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(1)::text").extract()
        item["gross_profit_rate"]=response.css(".cwzb > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7)::text").extract()
        item["net_margin"]=response.css(".cwzb > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4)::text").extract()
        item["net_assets"]=response.css(".cwzb > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)::text").extract()
        item["market_cap"]=response.css(".cwzb > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)::text").extract()
        yield item
