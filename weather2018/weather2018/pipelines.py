# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
dbuser = 'root'
dbpass = '1qaz2wsx#EDC'
dbname = 'weather'
dbhost = '127.0.0.1'
dbport = 3306
class Weather2018Pipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8")
        self.cursor = self.conn.cursor()
        #清空表：
        self.cursor.execute("truncate weather;")
        self.conn.commit()

    def process_item(self, item, spider):
        #curTime =  datetime.datetime.now()
        self.cursor.execute("""INSERT INTO weather (day,  wea, tem,win1,win2,power)
                            VALUES (%s, %s, %s,%s,%s,%s)""",
            (
                item['day'].encode('utf-8'),
                item['wea'].encode('utf-8'),
                item['tem'].encode('utf-8'),
                item['win1'].encode('utf-8'),
                item['win2'].encode('utf-8'),
                item['power'].encode('utf-8'),
            )
        )
        self.conn.commit()
        return item
