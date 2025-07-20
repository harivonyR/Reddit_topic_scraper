# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 16:46:40 2025

@author: BEST
"""

from script.reddit_topics import get_all_reddit_topic_list, save_list



# get all existing topics on reddit
all_reddit_topics = get_all_reddit_topic_list()
save_list(all_reddit_topics,"output/all_reddit_topics.csv")


# loop topics and get comment
