# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 20:45:43 2025

@author: BEST
"""

from script.piloterr import website_rendering
from bs4 import BeautifulSoup

# 1 - Fetch post data with post_link (we need this to fetch comments later)
#------------------------------------------------------------------------------
def scrape_comment(post_url,wait_in_seconds=10, scroll=0):
    print("-------------------------------")
    print(f"scraping comment from {post_url}")
    response = website_rendering(site_url = post_url,wait_in_seconds=wait_in_seconds,scroll=scroll)
    
    # Decode raw HTML
    clean_html = response.encode('utf-8').decode('unicode_escape')
    soup = BeautifulSoup(clean_html, 'html.parser')
    
    
    # get post details
    # ----------------
    post = soup.select_one("shreddit-post")

    post_details = {
        "comment_count": post.get("comment-count", "0"),
        "score": post.get("score", "0"),
        "author": post.get("author", "#N/A"),
        "text_content": post.select_one('div[slot="text-body"]').get_text(strip=True) if post.select_one('div[slot="text-body"]') else None,
        "title": post.select_one("h1").get_text(strip=True) if post.select_one("h1") else None,
    }

    # get comment details
    # --------------------
    comments = soup.select('shreddit-comment')
    
    # scrape data from comment
    comment_details = []
    for comment in comments:
        try:
            data = {
                "author": comment.get("author", "#N/A"),
                "time": comment.select_one("time")["datetime"] if comment.select_one("time") else None,
                "score": comment.get("score", "#N/A"),
                "depth": comment.get("depth", "#N/A"),
                "post_id": comment.get("postid", None),
                "parent_id": comment.get("parentid", None),
                "content_type": comment.get("content-type", None),
                "content": [p.get_text(strip=True) for p in comment.find_all("p")] or None
            }
            comment_details.append(data)
            print(f"author comment scrapped : {comment.get('author', '#N/A')}")
            
        except Exception as e:
            print(f"error: {e}")
            continue
        
    return {"post_details":post_details,"comment_details":comment_details}
    
    
if __name__=="__main__":
    reddit = "https://www.reddit.com/r/IndiaCricket/comments/1dniwap/aaron_finch_shuts_up_dk_during_commentary/"
    comment = scrape_comment(post_url=reddit,wait_in_seconds=5, scroll=2)
    