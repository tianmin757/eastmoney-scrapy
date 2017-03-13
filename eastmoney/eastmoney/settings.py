# -*- coding: utf-8 -*-

# Scrapy settings for eastmoney project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#import random

#random_num=random.uniform(5,18)
BOT_NAME = 'eastmoney'

SPIDER_MODULES = ['eastmoney.spiders']
NEWSPIDER_MODULE = 'eastmoney.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'eastmoney (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5 #random_num
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
             "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
             "Accept-Encoding":"gzip, deflate",
             "Referer":"http://www.eastmoney.com/",
             "Connection":"keep-alive"
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'eastmoney.middlewares.EastmoneySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'eastmoney.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

 

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'eastmoney.pipelines.EastmoneyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#USER_AGENT_LIST=['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',]

#启用Redis调度请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#默认请求序列化使用的是pickle,但是我们可以更改为其他类似的。PS:这玩意儿2.x可以用，3.x的不能用
#SCHEDULER_SERIALIZER="scrapy_redis.picklecompat"
#不清除Redis队列，这样可以暂停/恢复 爬取
SCHEDULER_PERSIST=True
#使用优先级调度请求队列(默认使用)
SCHEDULER_QUEUE_CLASS='scrapy_redis.queue.PriorityQueue'
#可选用的其他队列
#SCHEDULER_QUEUE_CLASS='scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS='scrapy_redis.queue.LifoQueue'
#最大空闲时间防止分布式爬虫因为等待而关闭
#SCHEDULER_IDLE_BEFORE_CLOSE=10
#序列化项目管道作为Redis Key存储
#REDIS_ITEMS_KEY='%(spider)s:items'
#默认使用ScrapyJSONEncoder进行项目序列化
#You can use any importable path to a callable object.
#REDIS_ITEMS_SERIALIZER='json.dumps'
#指定连接到Redis时使用的端口和地址（可选）
REDIS_HOST='127.0.0.1'
REDIS_PORT='6379'
#指定用于连接Redis的URL（可选）
#如果设置此项优先级高于REDIS_HOST和REDIS_PORT
#REDIS_URL='redis://user:pass@hostname:9001'
#自定义的Redis参数（连接超时之类的）
#REDIS_PARAMS={}
#自定义redis客户端类
#REDIS_PARAMS['redis_cls']='myproject.RedisClient'
#如果为True,则使用redis的'spop'进行操作
#如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
#REDIS_START_URLS_AS_SET=False
#RedisSpider和RedisCrawlSpider默认start_urls键
#REDIS_START_URLS_KEY='%(name)s:start_urls'
#设置redis使用utf-8之外的编码
#REDIS_ENCODING='latin1'


MONGODB_HOST='127.0.0.1'
MONGODB_PORT=27017
MONGODB_DBNAME="tianmin"
MONGODB_DOCNAME='eastbasic'

MYSQL_HOSTS='127.0.0.1'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASSWORD='root'
MYSQL_DB='test'
MYSQL_CHARSET='utf8'
