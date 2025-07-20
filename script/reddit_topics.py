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
import csv

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
        
    print ("------------------")
    print(f"{site_url} : found {len(topics_list)} topics")
    print ("------------------")
    
    return topics_list


def get_all_reddit_topic_list():
    letter_list = get_topic_letter_link()
    
    page_list = [] # all topics available in reddit
    for letter_link in  letter_list :
        pages = get_topic_page_list(letter_link)
        page_list.extend(pages)
        
    full_topics_list = []
    for page in page_list :
        topics = get_topic_list(page)
        full_topics_list.extend(topics)     
       
    print(f"> all topics found : {len(full_topics_list)}")
    return full_topics_list


def save_list(full_topics_list,destination="output/all_reddit_topics.csv"):
    """
    Save topics to CSV file. Overwrites existing file.
    Each item should be a dict: {topic: link}.
    """
    with open(destination, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["topic", "link"])  # header

        for topic_dict in full_topics_list:
            for topic, link in topic_dict.items():
                writer.writerow([topic, link])  # write row
    print("file saved !")
    
# single test process /debuggin step by step
def test():
    # Test topic_list with a sample, here topics starting with "a", page:1
    first_topic_section = "https://www.reddit.com/topics/a-1/"
    
    topics_list = get_topic_list(site_url=first_topic_section) # topics in one section
    print(f"topics_list = {topics_list}")
    
    letter_list = get_topic_letter_link() # this start by default with the first section of the topic list
    print(f"letter_list = {letter_list}")
    
    page_list = get_topic_page_list(site_url=first_topic_section)
    print(f"page_list = {page_list}")
    pass

# get all reddit topics with link
if __name__=="__main__":
    full_topics_list = get_all_reddit_topic_list()
    save_list(full_topics_list,destination="output/all_reddit_topics.csv")
    