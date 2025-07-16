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

topics_link = "https://www.reddit.com/t/american_top_team/"
response = crawl(query=topics_link)


# Decode raw html
#----------------------------

clean_html = response.encode('utf-8').decode('unicode_escape')
#print(clean_html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(clean_html, 'html.parser')


# Select all posts
#----------------------------
articles = soup.select('article')
#print(articles)

# get post details
for article in articles :
    #article = articles[0]   # get a sample for the test
    article_title = article["aria-label"]
    article_author = article.find("shreddit-post")["author"]
    article_link = article.find('a',href=True)["href"]
    article_date = article.find('shreddit-post')["created-timestamp"]
    article_total_comment = article.find('shreddit-post')["comment-count"]
    article_score = article.find('shreddit-post')["score"]
    
    print(f"date : {article_date}")
    print(f"author : {article_author}")
    print(f"score : {article_score}")
    print(f"title : {article_title}")
    print(f"relative link : {article_link}")
    print(f"total comment : {article_total_comment}")
    
    print("-----------------------")

