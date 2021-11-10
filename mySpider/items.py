# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


#用于定义爬取的字段
import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #老师姓名  //div[@class='main_mask']h2/text()
    name = scrapy.Field()
    #职称 //div[@class='main_mask']/h2/span
    title = scrapy.Field()
    #入职时间 //div[@class='main_mask']/h3
    date = scrapy.Field()
    #标签 //div[@class='main_bot']/h3
    tip = scrapy.Field()
    pass
