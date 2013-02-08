#-*- coding: utf-8 -*-

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from scrapy.exceptions import NotConfigured
import os

class MyExporter(object):

	def __init__(self, settings):
		#here exist two variant
		#file with My_Exporter_URI exist: this is the case of a CsvItemExporter instance initilized with include_headers_line=False
		#file with My_Exporter_URI doesn't exist: is the case of include_headers_line=True
		self.filename = settings['My_Exporter_URI']
		include_headers_line = False if os.path.isfile(self.filename) else True
		self.fileCsv = open(self.filename, 'ab')
		self.exporter = CsvItemExporter(self.fileCsv, include_headers_line=include_headers_line)
		
	


	@classmethod
	def from_crawler(cls, crawler):
		o = cls(crawler.settings)
		crawler.signals.connect(o.item_scraped, signals.item_scraped)
		crawler.signals.connect(o.close_spider, signals.spider_closed)
		return o

	def item_scraped(self, item, spider):
		self.exporter.export_item(item)
		return item

	def close_spider(self, spider):
		self.fileCsv.close()
