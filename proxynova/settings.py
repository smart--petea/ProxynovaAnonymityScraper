# Scrapy settings for proxynova project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'proxynova'

SPIDER_MODULES = ['proxynova.spiders']
NEWSPIDER_MODULE = 'proxynova.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'proxynova (+http://www.yourdomain.com)'
LOG_FILE = 'crawler.log'
SPIDER_MODULES = ['proxynova.spiders.SpiderIno']
My_Exporter_URI = '/export.csv'
CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY = 1
EXTENSIONS = {
			'proxynova.My_Exporter.MyExporter': 0
				}

ITEM_PIPELINES = ['proxynova.pipelines.ProxynovaPipeline']
