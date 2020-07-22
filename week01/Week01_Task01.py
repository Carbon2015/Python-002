# 作业一：
# 安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
# 猫眼电影网址： https://maoyan.com/films?showType=3

import requests
from bs4 import BeautifulSoup as BS
import pandas as PD

targetUrl = "https://maoyan.com/films?showType=3"

#增加cookie字段，否则可能去到”验证中心“页面。
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
          "cookie":"uuid=33119590CC2811EA989D8534BBE132DAE1777F37D0574C959B3EB84DE37B0413;"}

#使用requests获取目标页面response
response = requests.get(targetUrl, headers = header)

#使用BeautifulSoup来parse response为“BeautifulSoup”对象。参见https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
parsedData = BS(response.text, "html.parser")

#最总结果的List，为pandas输出做准备
resultList = []

#找到指定class的div标签，limit可以限制返回个数。
for movie in parsedData.find_all("div", class_="channel-detail movie-item-title", limit=10):

    #存储每个电影的名称，类型，上映时间为list
    tempResult = []

    ##记录电影名称到list
    tempResult.append(movie["title"])

    #获取每个电影的链接后，拼接url，打开下层页面。
    response_L2 = requests.get(str("https://maoyan.com" + movie.find("a")["href"]), headers = header)
    parsedData_L2 = BS(response_L2.text, "html.parser")

    #因为电影类型数量不固定，需要for in遍历所有类型。
    for movieType in parsedData_L2.find("div", class_="movie-brief-container").find("ul").find("li").find_all("a"):

        #记录电影类型到list
        tempResult.append(movieType.get_text().strip())

    #记录电影上映时间到list
    #多次find找到目标的唯一路径。
    #.find_all("li")[2] 让我们直接找第三个li而不用遍历。
    #.contents[0] 是因为find_all返回的是tag的list。tag的 .contents 属性可以将tag的子节点内容以列表的方式输出。或者使用get_text()也一样。
    tempResult.append(parsedData_L2.find("div", class_="movie-brief-container").find("ul").find_all("li")[2].contents[0][0:10])

    #记录电影信息到最终result列表
    resultList.append(tempResult)

#把list转为pandas的DataFrame
movieFile = PD.DataFrame(data = resultList)

#写DataFram为csv文件。中文系统使用GBK编码，英文可以使用utf-8
movieFile.to_csv("./MaoYanMovieTop10.csv", encoding="GBK", index=False, header=False)