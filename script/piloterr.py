# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:25:42 2025

@author: BEST
"""

from credential import x_api_key
import requests

def website_crawler(query):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":query}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    return response.text

def website_renderer(query):

    url = "https://piloterr.com/api/v2/website/rendering"
    
    # url for test
    querystring = {"query":"https://www.reddit.com/r/MMA/comments/syis7n/did_any_mma_team_ever_had_a_better_year_than/","wait_in_seconds":"20"}
    
    headers = {"x-api-key": x_api_key}
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #print(response.text)
    return response.text
        
    
def test():
    pass