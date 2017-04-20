#coding:utf-8
'''
Created on 2016-3-30

@author: zybang
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/item/
        links = soup.find_all('a', href=re.compile("/item/"))
        # /view/123.html
        #soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            #print new_full_url
        return new_urls
        
    def _get_new_link_entry(self, page_url, soup):
        new_links = []
        links = soup.find_all('a', href=re.compile("/item/"))
        # /view/123.html
        #soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            link_entry = {}
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            link_entry['url'] = new_full_url;
            link_entry['title'] = link.get_text()
            new_links.append(link_entry)
            #print new_full_url
        return new_links 
            
    def _get_new_data(self, page_url, soup):
        res_data = {} #字典Dwict={'name':'wzb', 'age':'23'}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        new_link_entry = self._get_new_link_entry(page_url, soup)
        return new_urls, new_data, new_link_entry
    



