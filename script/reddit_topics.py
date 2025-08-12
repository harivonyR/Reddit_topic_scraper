# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:24:06 2025

@author: harivonyratefiarison

This script scrapes all available Reddit topics with their links.

"""

from script.piloterr import website_crawler
from bs4 import BeautifulSoup
import csv
import os

def get_letter_pages():
    """
    Get all topic sections by letter (A-Z).
    Each link points to a paginated topic list.
    """
    site_url = "https://www.reddit.com/topics/a-1/"

    response = website_crawler(site_url=site_url)
    clean_html = response.encode('utf-8').decode('unicode_escape')
    soup = BeautifulSoup(clean_html, 'html.parser')

    links = soup.find_all("a", attrs={"class": "page-letter"})
    letters_href = ["https://www.reddit.com" + link.get("href") for link in links]
    letters_href.insert(0, site_url)

    print(f"> all topics found by lettre : \n {letters_href}")
    print("\n\n")
    return letters_href

def get_subpages(site_url):
    """
    Get all paginated pages for a given letter section.
    Includes the first page.
    """
    response = website_crawler(site_url=site_url)
    clean_html = response.encode('utf-8').decode('unicode_escape')
    soup = BeautifulSoup(clean_html, 'html.parser')

    pages = soup.select("div.digit-pagination.top-pagination a.page-number")
    pages_href = ["https://www.reddit.com" + page.get("href") for page in pages]
    pages_href.insert(0, site_url)

    print(f"> found topic pages and subpage : {pages_href}")
    return pages_href

def scrape_topics(site_url):
    """
    Get all topics and links from a topic page.
    Returns a list of dicts: [{topic: link}, ...]
    """
    response = website_crawler(site_url=site_url)
    clean_html = response.encode('utf-8').decode('unicode_escape')
    soup = BeautifulSoup(clean_html, 'html.parser')

    topics = soup.select('a.topic-link')
    topics_list = []

    for topic in topics:
        text = topic.get_text(strip=True)
        href = topic.get('href')
        print(f"{text} : {href}")
        topics_list.append({text: href})

    print("------------------")
    print(f"{site_url} : found {len(topics_list)} topics")
    print("------------------")
    return topics_list

def scrape_all():
    """
    Collect all topics across all letter sections and pages.
    Returns a flat list of dicts: [{topic: link}, ...]
    """
    letter_list = get_letter_pages()

    page_list = []
    for letter_link in letter_list:
        pages = get_subpages(letter_link)
        page_list.extend(pages)

    full_topics_list = []
    for page in page_list:
        topics = scrape_topics(page)
        full_topics_list.extend(topics)

    print(f"> all topics found : {len(full_topics_list)}")
    return full_topics_list

def save_csv(full_topics_list, destination="output/all_reddit_topics.csv"):
    """
    Save topics to CSV. Overwrites existing file.
    Each item = {topic: link}
    """
    # create the output folder if it doesn't exist yet
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    with open(destination, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["topic", "link"])

        for topic_dict in full_topics_list:
            for topic, link in topic_dict.items():
                writer.writerow([topic, link])

    print(f"> File saved to {destination}")


def debug():
    """
    Run step-by-step test with fixed page (a-1).
    Use for debugging individual functions.
    """
    first_topic_section = "https://www.reddit.com/topics/a-1/"

    topics_list = scrape_topics(site_url=first_topic_section)
    print(f"topics_list = {topics_list}")

    letter_list = get_letter_pages()
    print(f"letter_list = {letter_list}")

    page_list = get_subpages(site_url=first_topic_section)
    print(f"page_list = {page_list}")

if __name__ == "__main__":
    
    full_topics_list = scrape_all() # scrape all existing reddit topic
    save_csv(full_topics_list, destination="output/all_reddit_topics.csv")
