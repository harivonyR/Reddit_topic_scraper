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

def website_renderer(site_url):
    
    url = "https://piloterr.com/api/v2/website/rendering"
    
    querystring = {"query":site_url,"wait_in_seconds":"20"}
    
    headers = {"x-api-key": x_api_key}
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    #print(response.text)
    return response.text
        
    
def test():
    # redering OK
    #link1 = "https://www.comparably.com/companies/airbus"
    # redering NOK
    link2 = "https://www.reddit.com/r/movies/comments/s4phxj/i_watched_a_beautiful_day_in_the_neighborhood/"
    
    response = website_renderer(site_url=link2)
    print(response)
    print("test ends !")
    
    pass