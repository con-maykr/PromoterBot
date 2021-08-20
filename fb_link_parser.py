# facebook event link scraper/parser

import re
from bs4 import BeautifulSoup, SoupStrainer
import requests

url1 = "https://m.facebook.com/pg/shookatkremwerk/events"
url2 = "https://m.facebook.com/pg/kremwerk/events/"
url3 = "https://m.facebook.com/pg/studiofourfour/events/"

FULL_URLS = []

def get_links(url):

    # Pull down the HTML
    response = requests.get(url)

    # Iterate through every <a> tag, filtering to only pull hrefs (hyperlinks)
    # for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a', href=True)):
        #print(link['href'])
        #SEEN_URLS.append(link['href'])
        #if url in link['href'] and link['href'] not in SEEN_URLS:
            #get_links(link['href'])

    # Parse the HTML we pulled down and filter all hyperlinks out
    soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a', href=True))
    
    # Iterate through all of the links with "events" in them
    for link in soup.find_all(href=re.compile(r'\/events\/[^/?]*')):
    
        #print("Match:")
        #print(link.get('href'))
        
        # Regex to pull the useful stuff out of the link
        suffix = re.search(r'\/events\/[^/?]*', link.get('href'))[0]
        
        # Apphend it to a non-mobile facebook link
        full = "https://www.facebook.com" + suffix
        
        if full not in FULL_URLS:
            FULL_URLS.append(full)
        
        #print(full)
  
if __name__ == '__main__':
    get_links(url2)
    
    for link in FULL_URLS:
        print(link)