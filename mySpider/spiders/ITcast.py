
import scrapy
#从mySpider的items文件引用MyspiderItem类
from mySpider.items import MyspiderItem


class TycSpider(scrapy.Spider):
    # 爬虫名称,scrapy crawl 必须参数
    name = 'ITcast'
    # 爬虫范围，可选参数
    allowed_domains = ['http://www.itcast.cn']
    # 初始爬虫地址,可以是多个地址，爬虫执行的第一个请求从这里开始
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        nodeList = response.xpath("//div[@class='main_mask']")
        tips = response.xpath("//div[@class='main_bot']/h3/text()")
        items = []
        for i, node in enumerate(nodeList):
            item = MyspiderItem()
            #.extract()将xpath对象转换为Unicode字符串
            name = node.xpath("./h2/text()").extract()
            title = node.xpath("./h2/span/text()").extract()
            date = node.xpath("./h3/text()").extract()
            #tip = tips.extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['date'] = date[0]
            #item['tip'] = tip[i]
            items.append(item)
            print(item)

        return items

        #pass
