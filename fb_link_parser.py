# facebook event link scraper/parser

import re
from bs4 import BeautifulSoup, SoupStrainer
import requests
        
def get_links(url):
    
    FULL_URLS = []
    
    headers = {'accept':'text/html'} 
    
    r = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    raw_links = soup.find_all(href=re.compile(r'\/events\/[^/?]*'))
    
    for link in raw_links:
        suffixes = re.findall(r'\/events\/[^/?]*', link.get('href'))
        
        for s in suffixes:
            
            full = "https://www.facebook.com" + s
            
            if full not in FULL_URLS:
                FULL_URLS.append(full)
                
    return FULL_URLS
  

