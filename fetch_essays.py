#!/usr/bin/env python3

from bs4 import BeautifulSoup

import requests
import sys
import pprint

# Setup
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")
pp = pprint.PrettyPrinter(indent=4)
    
def find_nth_occurrence(text, sub, n):
    if n == 1:
        return text.find(sub)
    start = text.find(sub)
    return find_nth_occurrence(text[start + 1:], sub, n - 1)

base_url = "http://www.paulgraham.com/"
r  = requests.get("http://www.paulgraham.com/articles.html")
data = r.text
articles = {}

soup = BeautifulSoup(data, "html.parser")

# Get List of Articles to scrape. Hacky but works
fonts = soup.find_all('font')
for f in fonts:
    article_anchor_tag = f.find('a')
    anchor_string = str(article_anchor_tag)
    ts, te = anchor_string.find('>'), find_nth_occurrence(anchor_string, '<', 2)
    us, ue = find_nth_occurrence(anchor_string, '=', 1), find_nth_occurrence(anchor_string, '>', 1)
    title = anchor_string[ts + 1:te + 1]
    url = base_url + anchor_string[us + 2:ue - 1]
    articles[title] = url
# pp.pprint(articles)

for k, v in articles.items():
    r  = requests.get(v)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    fonts = soup.find_all('font')
    for f in fonts:
        article = open(k.replace(" ", "").replace("/", "") + ".html","w+")
        # article.write(str(f))
        pp.pprint(str(f))
