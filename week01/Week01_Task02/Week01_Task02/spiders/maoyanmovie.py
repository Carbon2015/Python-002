# 作业二：
# 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
# 猫眼电影网址： https://maoyan.com/films?showType=3
# 要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。

import scrapy
from scrapy.selector import Selector
from Week01_Task02.items import Week01Task02Item


class DoubanMovie(scrapy.Spider):
    name = "mymovie"
    allowed_domains = ["maoyan.com"]
    start_urls = ["https://maoyan.com/films?showType=3"]

    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/83.0.4103.116 Safari/537.36",
            "cookie": "uuid=33119590CC2811EA989D8534BBE132DAE1777F37D0574C959B3EB84DE37B0413;"}
        yield scrapy.Request(url=url, headers=header, callback=self.parse)

    def parse(self, response):
        # 裁剪之要前10个Selector
        movies = response.xpath('//div[@class="movie-hover-info"]')[:10]
        # 遍历Selector集合。因为movie仍然是Selector，可以继续用xpath方法。
        for movie in movies:
            # 创建pipeline用的item。记得去items.py先声明。然后import到本py。
            item = Week01Task02Item()
            # .//从当前节点乡下找子孙。如果此处用//则仍然从根节点做模糊查找。
            item["name"] = movie.xpath('.//div[@class="movie-hover-title"]/@title').get().strip()
            # /following-sibling::用法参见W3C XPath Axes. https://www.w3school.com.cn/xpath/xpath_axes.asp
            item["type"] = movie.xpath('.//div[@class="movie-hover-title"]/'
                                       'span[@class="hover-tag"]/following-sibling::text()').get().strip()
            item["date"] = movie.xpath('.//div[@class="movie-hover-title movie-hover-brief"]/'
                                       'span[@class="hover-tag"]/following-sibling::text()').get().strip()
            yield item
