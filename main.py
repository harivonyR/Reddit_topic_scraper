# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 16:46:40 2025

@author: BEST
"""

from script.reddit_topics import scrape_all, save_csv
from script.reddit_posts import scrape_post
from script.reddit_comments import scrape_comment

#-------------------------------------------------
# 1 - get all links of existing topics on reddit
#-------------------------------------------------
all_reddit_topics = scrape_all()                           # scrape all existing topics with link
save_csv(all_reddit_topics,"output/all_reddit_topics.csv") # save links in a csv file 


#-------------------------------------------------
# 2 - Scrape post present on a topic link 
#-------------------------------------------------
topic_link = "https://www.reddit.com/t/american_top_team/"
posts = scrape_post(topic_link,wait_in_seconds=10, scroll=0)


#-------------------------------------------------
# 3 - scroll and get post in a topic 
#-------------------------------------------------
post_link = "https://www.reddit.com/r/IndiaCricket/comments/1dniwap/aaron_finch_shuts_up_dk_during_commentary/"
comment = scrape_comment(post_url=post_link,wait_in_seconds=5, scroll=2)



# for those who whant data
def reddit_scraping_all(output_folder="output", wait=5, scroll=2):
    # Step 1 - Get all reddit topics and links
    all_reddit_topics = scrape_all()
    save_csv(all_reddit_topics, f"{output_folder}/all_reddit_topics.csv")

    all_results = []

    # Step 2 - Loop through each topic and scrape posts
    for topic, link in all_reddit_topics.items():
        try:
            posts = scrape_post(link, wait_in_seconds=wait, scroll=scroll)
            print(f"Scraped {len(posts)} posts from topic: {topic}")

            # Step 3 - For each post, scrape comments
            for post in posts:
                try:
                    data = scrape_comment(post_url=post, wait_in_seconds=wait, scroll=scroll)
                    all_results.append(data)
                except Exception as e:
                    print(f"Error scraping comments from post: {post}\n{e}")

        except Exception as e:
            print(f" Error scraping posts from topic: {topic}\n{e}")

    return all_results