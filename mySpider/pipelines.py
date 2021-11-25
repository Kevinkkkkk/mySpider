# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

#管道，储存数据。可以创建多个类，用来做不同数据格式的处理，此为json
class MyspiderPipeline:
    #初始化函数，仅在开始运行一次
    def __init__(self):
        self.f = open('ITcast_pipeline.json','wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False) + '\n'
        self.f.write(content.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.f.close()