# -*- coding: utf-8 -*-
"""
Main script to test and run full Reddit scraping pipeline using Piloterr API.

Modules:
    - reddit_topics: scrape all subreddit topics
    - reddit_posts: extract posts from each topic
    - reddit_comments: get comments from individual post URLs

Created on Sun Jul 20 16:46:40 2025
@author: BEST
"""

from script.reddit_topics import scrape_all, save_csv
from script.reddit_posts import scrape_post
from script.reddit_comments import scrape_comment


# -------------------------------------------------------
# STEP-BY-STEP TEST: scrape topics, posts, and comments
# -------------------------------------------------------

if __name__ == "__main__":
    print("Step 1: Scraping all Reddit topics...")
    all_reddit_topics = scrape_all()
    save_csv(all_reddit_topics, "output/all_reddit_topics.csv")
    print(f"{len(all_reddit_topics)} topics scraped and saved.")

    print("\nStep 2: Scraping posts from a single topic...")
    sample_topic_link = "https://www.reddit.com/t/american_top_team/"
    posts = scrape_post(sample_topic_link, wait_in_seconds=10, scroll=0)
    print(f"{len(posts)} posts scraped from topic.")

    print("\nStep 3: Scraping comments from a sample post...")
    sample_post_link = "https://www.reddit.com/r/IndiaCricket/comments/1dniwap/aaron_finch_shuts_up_dk_during_commentary/"
    comments = scrape_comment(post_url=sample_post_link, wait_in_seconds=5, scroll=2)
    print(f"{len(comments)} comments scraped from sample post.")


# -------------------------------------------------------
# FULL PIPELINE: loop through topics > posts > comments
# -------------------------------------------------------

def reddit_scraping_all(output_folder="output", wait=5, scroll=2):
    """
    Runs the full Reddit scraping pipeline:
    1. Scrape all topics and save them.
    2. For each topic, scrape posts.
    3. For each post, scrape comments.

    Args:
        output_folder (str): Folder to save CSVs.
        wait (int): Wait time between requests (seconds).
        scroll (int): Number of scroll iterations for dynamic loading.

    Returns:
        list: A list of all comments scraped across all posts.
    """
    print("\n[RUNNING] Full Reddit Scraping Pipeline")
    all_reddit_topics = scrape_all()
    save_csv(all_reddit_topics, f"{output_folder}/all_reddit_topics.csv")
    print(f"✅ {len(all_reddit_topics)} topics saved to CSV.")

    all_results = []

    for topic, link in all_reddit_topics.items():
        print(f"\n[TOPIC] {topic} - {link}")
        try:
            posts = scrape_post(link, wait_in_seconds=wait, scroll=scroll)
            print(f"> {len(posts)} posts found.")

            for post in posts:
                try:
                    comments = scrape_comment(post_url=post, wait_in_seconds=wait, scroll=scroll)
                    all_results.append(comments)
                    print(f" Scraped {len(comments)} comments from post.")
                except Exception as e:
                    print(f" Error scraping comments from {post}: {e}")

        except Exception as e:
            print(f" TOPIC scraping {topic} : error {e}")

    print("\n✅ Pipeline completed.")
    return all_results
