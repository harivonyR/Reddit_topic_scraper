# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:25:42 2025

@author: BEST
"""

from credential import x_api_key
import requests

def website_crawler(site_url):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":site_url}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    return response.text


import requests

def website_rendering(site_url, wait_in_seconds=20, scroll=0):
    """
    Render a website using Piloterr API.
    Supports optional scroll to bottom.
    """
    url = "https://piloterr.com/api/v2/website/rendering"
    querystring = {"query": site_url, "wait_in_seconds": str(wait_in_seconds)}
    headers = {"x-api-key": x_api_key}  # Assure-toi que x_api_key est défini globalement

    # we don't need to scroll
    if scroll == 0:
        response = requests.get(url, headers=headers, params=querystring)
    
    # debug scrolling to bottom
    else:
        # smooth scrolling to the bottom
        smooth_scroll = [
            {
                "type": "scroll",
                "x": 0,
                "y": 1000,
                "duration": 2,
                "wait_time_s": 1
            },
            {
                "type": "scroll",
                "x": 0,
                "y": 2000,
                "duration": 3,
                "wait_time_s": 4
            },
            {   
                "type": "scroll_to_bottom",
                "duration": 4,
                "wait_time_s": 10
            }
        ]

        # repeate scrolling
        #repeated_instructions = smooth_scroll * scroll # debug : multiple insctruction not supported

        instruction = {
            "query": site_url,
            "wait_in_seconds": str(wait_in_seconds),
            "browser_instructions": [
                {
                    "type": "scroll",
                    "x": 0,
                    "y": 2000,
                    "duration": 3,
                    "wait_time_s": 4
                }]
        }

        response = requests.post(url, headers=headers, json=instruction)

    return response.text

    
def test():
    # redering OK
    comparably = "https://www.comparably.com/companies/airbus"
    topic_url = "https://www.reddit.com/t/a_beautiful_day_in_the_neighborhood/"
    post_url = "https://www.reddit.com/r/movies/comments/s4phxj/i_watched_a_beautiful_day_in_the_neighborhood/"
    
    response = website_rendering(site_url=comparably,scroll=1)
    
    print(response)
    print("test ends !")
    
    pass


if __name__ == "__main__":
    test()