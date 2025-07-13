# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 11:03:05 2025

@author: harivonyratefiarison
"""


# Fetch HTML data


from credential import x_api_key
import requests

url = "https://piloterr.com/api/v2/website/crawler"

headers = {"x-api-key": x_api_key}
querystring = {"query":"https://www.reddit.com/r/announcements/"}

response = requests.request("GET", url, headers=headers,params=querystring)

print(response.text)


# Extract data (subject/topic)
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')

# selector : document.querySelectorAll('[slot="full-post-link"]')
# postTitle = document.querySelectorAll('[slot="full-post-link"]')[5].innerText

all_posts = soup.select('[slot="full-post-link"]')
