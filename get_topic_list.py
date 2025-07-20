# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:24:06 2025

@author: harivonyratefiarison

about : This script scrap all available reddit topic list with link

"""

# Get data
#----------------------------
from script.piloterr import website_crawler
from bs4 import BeautifulSoup

# Get topic by listing starting letter with links
def get_topic_letter_link():
    # start by default with the first topic "a" page 1
    site_url = "https://www.reddit.com/topics/a-1/"
    
    response = website_crawler(site_url=site_url)
    clean_html = response.encode('utf-8').decode('unicode_escape')
    
    soup = BeautifulSoup(clean_html, 'html.parser')
    
    links = soup.find_all("a", attrs={"class": "page-letter"})
    
    # get full link 
    letters_href = ["https://www.reddit.com"+link.get("href") for link in links]
    
    # insert our first letter
    letters_href.insert(0, site_url)

    print(letters_href)
    return letters_href

# Get list of all existing page starting with a letter
def get_topic_page_list(site_url):
    
    #site_url = "https://www.reddit.com/topics/a-1/"
    response = website_crawler(site_url=site_url)
    clean_html = response.encode('utf-8').decode('unicode_escape')
    
    soup = BeautifulSoup(clean_html, 'html.parser')
    pages = soup.select("div.digit-pagination.top-pagination a.page-number")
    
    pages_href = ["https://www.reddit.com"+page.get("href") for page in pages]
    
    pages_href.insert(0, site_url)
    
    print(pages_href)    
    return pages_href

def get_topic_list(site_url):
    response = website_crawler(site_url=site_url)

    # Decode raw html
    clean_html = response.encode('utf-8').decode('unicode_escape')
    
    # Extracting topics and links
    soup = BeautifulSoup(clean_html, 'html.parser')
    
    # Select topics element :
    topics = soup.select('a.topic-link')
    
    # Build structured data 
    topics_list = []  
    for topic in topics:
        text = topic.get_text(strip=True)
        href = topic.get('href')
        print(f"{text} : {href}")
        topics_list.append({text: href})
    
    return topics_list

# test process step by step
def test():
    # Test topic_list with a sample, here topics starting with "a", page:1
    first_topic_section = "https://www.reddit.com/topics/a-1/"
    
    topics_list = get_topic_list(site_url=first_topic_section) # topics in one section
    
    letter_list = get_topic_letter_link() # this start by default with the first section of the topic list
    page_list = get_topic_page_list(site_url=first_topic_section)
    
    pass

# get all reddit topics with link
if __name__=="__main__":
    
    letter_list = get_topic_letter_link()
    
    full_topics_list = [] # all topics available in reddit
    
    for letter_link in  letter_list :
        pages = get_topic_page_list(letter_link)
        
        full_topics_list.append(pages)
        
    pass