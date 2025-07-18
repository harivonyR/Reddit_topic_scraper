# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:03:05 2025

@author: harivonyratefiarison

about : This code scrape reddit post found on a "topic"

Topic Link : https://www.reddit.com/topics/a-1/

"""


# 1 - Fetch HTML data (crawler)
#----------------------
from script.piloterr import website_crawler
from bs4 import BeautifulSoup

# Get post from a redit topics URL
def get_post(url="https://www.reddit.com/t/american_top_team/"):
    
    topics_link = url      # url is a topic link on reddit
    response = website_crawler(query=topics_link)
    
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

def get_comment(url):
    # scraping comment
    # ----------------
    
    # topics = https://www.reddit.com/t/american_top_team/
    # post_link = /r/MMA/comments/syis7n/did_any_mma_team_ever_had_a_better_year_than/
    
    # create a link to access the post with comment
    #reddit_post =  "https://www.reddit.com"+post["link"]
    
    #crete a sample link
    
    reddit_post = "https://www.reddit.com/r/MMA/comments/syis7n/did_any_mma_team_ever_had_a_better_year_than/"
    
    response = website_crawler(query = reddit_post)
    
    # Decode raw HTML
    clean_html = response.encode('utf-8').decode('unicode_escape')
    soup = BeautifulSoup(clean_html, 'html.parser')
    
    # select comments
    comments = soup.find_all('div') #attrs={'slot': 'comment'})
    


def test():
    reddit_topic = "https://www.reddit.com/t/american_top_team/"
    posts = get_post(url=reddit_topic)
    post = posts[5]
        
    reddit_post =  "https://www.reddit.com"+post["link"]
    
    #comments = get_comment(post)
    
    
    
