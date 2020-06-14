# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import QqhywItem


class HySpider(scrapy.Spider):
    name = 'hy'
    # allowed_domains = ['qqhyw.com']

    company_list = 'http://www.qqhyw.com/company/'
    page_list = 'http://www.qqhyw.com/page/'

    def start_requests(self):
        yield scrapy.Request(url=self.company_list, callback=self.parse_company)
        yield scrapy.Request(url=self.page_list, callback=self.parse_page)

    def parse_company(self, response):
        a_list = response.xpath('//div[@class="dirlist"]//a/@href').getall()
        for a_url in a_list:
            yield scrapy.Request(url=a_url, callback=self.parse_com_list_page)


    def parse_page(self, response):
        add_list = response.xpath('//div[@class="dirlist"]//a/@href').getall()
        for add_url in add_list:
            yield scrapy.Request(url=add_url, callback=self.parse_com_list_page)

    def parse_com_list_page(self, response):
        com_list = response.xpath('//ul[@class="comlist"]/li/div/a/@href').getall()
        for com_url in com_list:
            yield scrapy.Request(url=com_url,callback=self.parse_detail)
        next_pages = response.xpath('//div[@class="pageLink"]/a/@href').getall()
        if next_pages:
            for next_page in next_pages:
                yield scrapy.Request(url=next_page, callback=self.parse_com_list_page)

    def parse_detail(self, response):
        title = response.xpath('//h1/text()').get()
        main_business = response.xpath('//div[@class="companydetail"]/div[@class="keyword"]/text()').get()
        main_business = main_business[5:] if len(main_business)>7 else '暂未填写'

        address = response.xpath('//div[@class="contact px14"]/ul/li[1]/text()').get()
        if address:
            address = address[5:]
        zip_code = response.xpath('//div[@class="contact px14"]/ul/li[2]/text()').get()
        zip_code = zip_code[5:] if len(zip_code)>7 else '暂未填写'
        tel = response.xpath('//div[@class="contact px14"]/ul/li[3]/span[1]/text()').get()
        tel = tel if tel else '暂未填写'
        mobile = response.xpath('//div[@class="contact px14"]/ul/li[4]/span[1]/text()').get()
        mobile = mobile if mobile else '暂未填写'
        fox = response.xpath('//div[@class="contact px14"]/ul/li[5]/text()').get()[5:]
        fox = fox[5:] if len(fox)>7 else '暂未填写'
        context_name = response.xpath('//div[@class="contact px14"]/ul/li[6]/text()').get()
        if '先' in context_name:
            context_name = re.findall(r'：(.*?) 先', context_name)
        if '女' in context_name:
            context_name = re.findall(r'：(.*?) 女', context_name)
        context_name = context_name[0] if context_name else '暂未填写'

        # print(title, main_business)
        # print(zip_code)
        # print(tel,mobile)
        # print('fox:', fox)
        # print(address, context_name)

        item = QqhywItem()
        item['title'] = title
        item['main_business'] = main_business
        item['zip_code'] = zip_code
        item['tel'] = tel
        item['mobile'] = mobile
        item['fox'] = fox
        item['address'] = address
        item['context_name'] = context_name

        yield item


