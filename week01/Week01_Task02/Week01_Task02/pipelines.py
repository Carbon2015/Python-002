# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class Week01Task02Pipeline:
    def process_item(self, item, spider):
        # ”a"和“a+"都可以append写，但只有”a+“才可以读
        with open("./movies_work02.csv", "a", encoding="GBK") as f:
            f.write(item["name"] + "," + item["type"] + "," + item["date"] + "\n")
        return item
