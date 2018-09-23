from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json, codecs

MAX_POSTS = 8

# open connection to Expedia's Facebook posts page and fetch the page content
expedia_fb_posts_url = 'https://www.facebook.com/pg/expedia/posts/'
fb_connection = urlopen(expedia_fb_posts_url)
fb_html = fb_connection.read()
fb_connection.close()

# parse html using BeautifulSoup
fb_page_soup = soup(fb_html, "html.parser")

# find the specified number of FB posts based on element & class name
posts = fb_page_soup.findAll("div", {"class": "_1dwg _1w_m _q7o"}, limit=MAX_POSTS)

# declare a new list to hold details of each post
posts_list = []

# loop through posts and find each post's relevant content based on element & class name, then store results into the posts list
for index in range(len(posts)):
  # construct a dict containing relevant post data
  title = posts[index].find("span", {"class": "fcg"}).text
  timestamp = posts[index].find("span", {"class": "timestampContent"}).text
  text = posts[index].find("div", {"class": "_5pbx userContent _3576"}).text
  
  # append dict to list of posts
  posts_list.append({
    'title': title,
    'timestamp': timestamp,
    'text': text
  })

# open or create a txt file, and use json & codecs modules to write the posts object to it
# credit: https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
with open('expedia_fb_posts.txt', 'wb') as outfile:
  json.dump(posts_list, codecs.getwriter('utf-8')(outfile), ensure_ascii=False)