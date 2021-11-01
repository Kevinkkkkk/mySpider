import scrapy


class TycSpider(scrapy.Spider):
    # 爬虫名称,scrapy crawl 必须参数
    name = 'ITcast'
    # 爬虫范围，可选参数
    allowed_domains = ['http://www.itcast.cn']
    # 初始爬虫地址,可以是多个地址，爬虫执行的第一个请求从这里开始
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        nodeList = response.xpath("//div[@class='main_mask']")
        for node in nodeList:
            #
            name = node.xpath("/h2/text()")
            #
            title = node.xpath("/h2/span")
            #
            date = node.xpath("/h3")
            #
            tip = response.xpath("//div[@class='main_bot']/h3")
            print(tip)

        #pass
