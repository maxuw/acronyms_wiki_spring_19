# link extractor class

# CATEGORY_DIVS = ["mw-content-ltr",
#                  "mw-subcategories"]
# import httplib2
# from bs4 import BeautifulSoup  # , SoupStrainer
# from urllib.parse import urljoin

# import requests
# import urllib.request
# import time

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

from timeout import timeout


def type_page(url):

    if "pl.wikipedia.org" not in url:

        return "not a polish wikipedia page"

    if "https://" in url:
        url = url.replace("https://", "")

    elif "http://" in url:
        url = url.replace("http://", "")

    if "www." in url:
        url = url.replace("www.", "")

    url = url.replace("pl.wikipedia.org/", "")

    if "wiki/" not in url:

        return "wikipedia, but not an encyclopedia type of page"

    else:
        url = url.replace("wiki/", "")

        print(url)

        if "Kategoria:" in url:

            page_type = "category"

        elif "Portal:" in url:

            page_type = "portal_page"

        elif ":" not in url:
            page_type = "record"

        else:
            page_type = "unknown type of page" + url
            print(page_type + url)

        # print(page_type)
        return page_type


def return_links_within_div(url, div_name):
    http = httplib2.Http()
    status, response = http.request(url)

    soup = BeautifulSoup(response, 'html.parser')

    target_div = soup.find("div", id=div_name)

    links = target_div.find_all('a')

    list_links = []

    for a in links:
        link_relative = a.get("href")
        link_absolute = urljoin(url, link_relative)
        list_links.append(link_absolute)

    return list_links

def return_links_within_div(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    target_divs = soup.find_all("div", class_="mw-content-ltr")
    list_links = []

    for d in target_divs:
        links = d.find_all('a')



        for a in links:
            link_relative = a.get("href")
            link_absolute = urljoin(url, link_relative)
            list_links.append(link_absolute)
    return list_links

def links_with_connect_error(url):

    links = []
    while links == []:
        try:
            with timeout(seconds=3):
                links = return_links_within_div(url)

        except:
            print("can't connect")
    return links


def return_links_category(links_category=[], links_record=[]):
    links_category = links_category
    links_record = links_record

    while links_category != []:
        for l in links_category:
            links = return_links_within_div(l)
            links_category.remove(l)

            for link in links:
                if type_page(link) == "category":
                    links_category.append(link)

                elif type_page(link) == "record":
                    links_record.append(link)

        return_links_category(links_category, links_record)

    return links_record
