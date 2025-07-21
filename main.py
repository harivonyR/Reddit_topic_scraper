# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 16:46:40 2025

@author: BEST
"""

from script.reddit_topics import scrape_all, save_csv




# 0 - get all links of existing topics on reddit
#-------------------------------------------------
all_reddit_topics = scrape_all()

# save links in a csv file 
save_csv(all_reddit_topics,"output/all_reddit_topics.csv") 

# 1 - scroll and get post in a topic 
#-------------------------------------------------
