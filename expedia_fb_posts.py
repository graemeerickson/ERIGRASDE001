from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

MAX_POSTS = 8

# open connection to Expedia's Facebook posts page and fetch the page content
expedia_fb_posts_url = 'https://www.facebook.com/pg/expedia/posts/'
fb_connection = urlopen(expedia_fb_posts_url)
fb_html = fb_connection.read()
fb_connection.close()

# parse html using BeautifulSoup
fb_page_soup = soup(fb_html, "html.parser")

# find the first 8 FB posts based on element & class name
posts = fb_page_soup.findAll("div", {"class": "_1dwg _1w_m _q7o"}, limit=MAX_POSTS)

# declare a new object to hold details of each post
postsObj = {}

# loop through posts and find each post's relevant content based on element & class name, then store results into the posts object
for index in range(len(posts)):
  title = posts[index].find("span", {"class": "fcg"}).text
  timestamp = posts[index].find("span", {"class": "timestampContent"}).text
  text = posts[index].find("div", {"class": "_5pbx userContent _3576"}).text
  
  postsObj[index] = {
    'title': title,
    'timestamp': timestamp,
    'text': text
  }