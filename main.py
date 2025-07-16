# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:03:05 2025

@author: harivonyratefiarison

about : This code scrape reddit post found on a "topic"

Topic Link : https://www.reddit.com/topics/a-1/

"""


# 1 - Fetch HTML data (crawler)
#----------------------
from script.crawler import crawl

sample_topics = "https://www.reddit.com/t/american_top_team/"
response = crawl(query=sample_topics)

# Decode raw html
#----------------------------

clean_html = response.encode('utf-8').decode('unicode_escape')
#print(clean_html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(clean_html, 'html.parser')


# Select all posts
#----------------------------
articles = soup.select('article')

# get post details
for article in articles :

    article_title = article["aria-label"]
    article_link = article.find('shreddit-post')['content-href']
    article_author = article.find("shreddit-post")["author"]
    
    print(f"{article_title} : {article_link}")
    print("-----------------------")

