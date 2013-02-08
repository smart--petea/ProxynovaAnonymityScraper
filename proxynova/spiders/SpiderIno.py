#-*- coding: utf8 -*-

from scrapy.spider import BaseSpider
from scrapy import log
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from proxynova.items import ProxynovaItem
import re

reIpCompile = re.compile(r'document.write\(decode\("(.*)"\)\)')
rePortCompile = re.compile(r'>\s*(\d+)\s*</')
reCountryCompile = re.compile(r'/country-(.*?)/')
reAsdCompile = re.compile(r'asd')#will be replaced with 6
reZxcCompile = re.compile(r'zxc')#will be replaced with 8
reQweCompile = re.compile(r'qwe')#will be replaced with 2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def MyDecoder(ddd):
	ddd = reAsdCompile.sub('6', ddd)	
	ddd = reZxcCompile.sub('8', ddd)
	ddd = reQweCompile.sub('2', ddd)
	ddd = int(ddd)
	first = str(ddd >> 24)
	second = str((ddd >> 16) & 0xFF)
	third = str((ddd >> 8) & 0xFF)
	fourth = str(ddd & 0xFF)

	return '.'.join([first, second, third, fourth])





class SpiderIno(BaseSpider):
	name = 'proxynova'
	allowed_domains = ["www.proxynova.com"]
	
	def start_requests(self):
		CountryList = ['ru', 'br', 'cn', 'id', 'th', 've', 'eg', 'us', 'pe', 'tw', 'ae', 'in', 'ar', 'za', 'co', 'de', 'ua', 'hk', 'fr', 'mx', 'pl', 'bd', 'it', 'ec', 'gb', 'jp', 'nl', 'tr', 'cl', 'pk', 'ca', 'mn', 'cz', 'kr', 'my', 'kh', 'ma', 'rs', 'bn', 'ir', 'iq', 'hu', 'bg', 'es', 'vn', 'lb', 'ng', 'ro', 'eu', 'ph']
		for country in CountryList:
			yield Request("http://www.proxynova.com/proxy-server-list/country-"+country+"/")
		#yield Request("http://www.proxynova.com/")
		

	def parse(self, response):
		if response.status // 100 != 2:
			log.msg(message="SpiderIno, parse problem with url %s"% response.url, _level = log.ERROR)

		selText = HtmlXPathSelector(response).select("//div[@id='bla']//tbody/tr").extract()
		for tr in selText:
			if 'proxy_transparent' in tr:
				continue
			item = ProxynovaItem()
			item['ip'] = MyDecoder(reIpCompile.search(tr).group(1))
			item['port'] = rePortCompile.search(tr).group(1)
			item['country'] = reCountryCompile.search(tr).group(1)
			print(item)
			yield item

