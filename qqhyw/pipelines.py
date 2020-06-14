# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
pymysql.install_as_MySQLdb()

class QqhywPipeline(object):

    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            database='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.conn.ping(reconnect=True)
        self.cursor.execute('''INSERT INTO qqhyw(title, main_business, zip_code, tel, mobile, 
        fox, address, context_name) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''',
        (item['title'], item['main_business'], item['zip_code'], item['tel'], item['mobile'],
         item['fox'], item['address'], item['context_name']))
        self.conn.commit()
        return item

        # item['title'] = title
        # item['main_business'] = main_business
        # item['zip_code'] = zip_code
        # item['tel'] = tel
        # item['mobile'] = mobile
        # item['fox'] = fox
        # item['address'] = address
        # item['context_name'] = context_name

    def close(self, spider):
        self.cursor.close()
        self.conn.close()
