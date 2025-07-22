# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:03:05 2025

@author: harivonyratefiarison

about : This code scrape reddit post found on a "topic"

Topic Link : https://www.reddit.com/topics/a-1/

"""

from script.piloterr import website_crawler, website_rendering
from script.reddit_comments import scrape_comment
from bs4 import BeautifulSoup


# 1 - Fetch post data with post_link (we need this to fetch comments later)
#------------------------------------------------------------------------------
def scrape_post(topic_url,wait_in_seconds=10, scroll=2 ):
    print("------------------")
    print(f"scraping topics : {topic_url}")
    # url is a topic link on reddit
    response = website_rendering(topic_url,wait_in_seconds, scroll)
    
    # Decode raw HTML
    clean_html = response.encode('utf-8').decode('unicode_escape')
    
    soup = BeautifulSoup(clean_html, 'html.parser')
    
    # Select all posts
    articles = soup.select('article')
    
    posts = []
    
    for article in articles:
        try:
            shreddit_post = article.find("shreddit-post")
            post_link = "https://www.reddit.com"+article.find("a", href=True).get("href")
            post = {
                "title": article.get("aria-label","#N/A"),
                "author": shreddit_post.get("author","#N/A"),
                "link": post_link,
                "date": shreddit_post.get("created-timestamp","#N/A"),
                "comment_count": shreddit_post.get("comment-count", "#N/A"),
                "score": shreddit_post.get("score","#N/A")#,
                #"comment": scrape_comment(post_url=post_link,wait_in_seconds=5, scroll=2)
            }
            print(f"post scraped : {article.get('aria-label','#N/A')}")
            print("-------------------")
            posts.append(post)
            
        except Exception as e:
            print(f"Error parsing article: {e}")
    
    return posts


if __name__ == "__main__":
    # sample
    american_top_tem = "https://www.reddit.com/t/american_top_team/"
    posts = scrape_post(american_top_tem,wait_in_seconds=10, scroll=0)

    
    
    
