#coding:utf-8
'''
Created on 2016-3-30

@author: zybang
'''
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url) #将源URL加入newUrl容器
        while self.urls.has_new_url(): 
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data, new_link_entry = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                #self.outputer.collect_data(new_urls)
                self.outputer.collect_data(new_data)
                self.outputer.output_html(new_link_entry)
                if count == 3:
                    break
                
                count = count + 1 
            except Exception,e:  
                print Exception,":",e
        self.outputer.output_self_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)