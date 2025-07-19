# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:24:06 2025

@author: harivonyratefiarison

about : This script scrap all available reddit topic list with link

"""

# Get data
#----------------------------
from script.crawler import crawl

link = "https://www.reddit.com/topics/a-1/"
response = crawl(query=link)


# Decode raw html
#----------------------------
clean_html = response.encode('utf-8').decode('unicode_escape')


# Extracting topics and links
#----------------------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(clean_html, 'html.parser')

# select topics element :
topics = soup.select('a.topic-link')


# Build structured data 
topics_link = []  

for topic in topics:
    text = topic.get_text(strip=True)
    href = topic.get('href')
    print(f"{text} : {href}")
    topics_link.append({text: href})
    

# add page loop
