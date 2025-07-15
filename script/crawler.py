# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:25:42 2025

@author: BEST
"""

from credential import x_api_key
import requests

def crawl(query):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":query}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    return response.text