 import httplib2
from bs4 import BeautifulSoup, SoupStrainer



http = httplib2.Http()
status, response = http.request('https://pl.wikipedia.org/w/index.php?title=Kategoria:Choroby_genetyczne&pagefrom=Pyknodysostoza#mw-pages')

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        if link['href'][0:2] == "/w":
            link['href'] = "https://pl.wikipedia.org/" + link['href']
        print(link['href'])
