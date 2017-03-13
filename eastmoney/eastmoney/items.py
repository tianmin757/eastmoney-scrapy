# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class EastmoneyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    market_cap=Field()          #总市值
    net_margin=Field()          #净利润
    net_assets=Field()          #净资产
    gross_profit_rate=Field()   #毛利率
    ROE=Field()                 #净资产收益率
    stock_id=Field()            #股票代码
    name=Field()                #股票名称
