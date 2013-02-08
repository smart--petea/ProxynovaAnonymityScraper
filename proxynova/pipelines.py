# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals, log
from scrapy.xlib.pydispatch import dispatcher
import os, csv
from scrapy.exceptions import DropItem

class ProxynovaPipeline(object):
	def __init__(self):
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)


	def process_item(self, item, spider):
		if [item['ip'], item['port']] in self.memory:
			self.oldItems += 1
			raise DropItem
		else:
			self.newItems += 1
			self.memory.append([item['ip'], item['port']])

		return item

	def spider_opened(self, spider):
		filename = spider._crawler.settings['My_Exporter_URI']
		try:
			ffile = open(filename, 'r')	
		except IOError:
			self.memory = []
		else:
			self.memory = [[x[0], x[1]] for x in csv.reader(ffile)]
		finally:
			ffile.close()
	
		self.newItems = 0
		self.oldItems = 0


	def spider_closed(self, spider):
		log.msg(message="ProxynovaPipeline, spider_closed newItems = {0}, oldItems = {1}".format(self.newItems, self.oldItems))
