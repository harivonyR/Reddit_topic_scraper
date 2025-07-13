# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:03:05 2025

@author: harivonyratefiarison
"""

from credential import x_api_key
import requests

url = "https://piloterr.com/api/v2/website/crawler"

headers = {"x-api-key": x_api_key}

response = requests.request("GET", url, headers=headers)

print(response.text)

