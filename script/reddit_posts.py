# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:03:05 2025

@author: harivonyratefiarison

about : This code scrape reddit post found on a "topic"

Topic Link : https://www.reddit.com/topics/a-1/

"""

from script.piloterr import website_crawler, website_rendering
from bs4 import BeautifulSoup


# 1 - Fetch post data with post_link (we need this to fetch comments later)
#------------------------------------------------------------------------------
def scrape_post(topic_url):
    
    # url is a topic link on reddit
    response = website_rendering(site_url=topic_url)
    
    # Decode raw HTML
    clean_html = response.encode('utf-8').decode('unicode_escape')
    
    soup = BeautifulSoup(clean_html, 'html.parser')
    
    # Select all posts
    articles = soup.select('article')
    
    posts = []
    for article in articles:
        try:
            shreddit_post = article.find("shreddit-post")
            post = {
                "title": article.get("aria-label"),
                "author": shreddit_post.get("author"),
                "link": article.find("a", href=True).get("href"),
                "date": shreddit_post.get("created-timestamp"),
                "comment_count": shreddit_post.get("comment-count"),
                "score": shreddit_post.get("score")
            }
            posts.append(post)
        except Exception as e:
            print(f"Error parsing article: {e}")
    
    return posts


def test():
    american_top_tem = "https://www.reddit.com/t/american_top_team/"
    posts = scrape_post(topic_url=american_top_tem)
    post = posts[5]
        
    reddit_post =  "https://www.reddit.com"+post["link"]
    
    #comments = get_comment(post)
    
    
    
