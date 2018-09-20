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

# get each FB post based on class name
posts = fb_page_soup.findAll("div", {"class": "_1dwg _1w_m _q7o"}, limit=MAX_POSTS)