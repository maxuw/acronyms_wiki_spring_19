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

        # print(url)

        if "Kategoria:" in url:

            page_type = "category"

        elif "Portal:" in url:

            page_type = "portal_page"
        elif "Wikimedia_Commons" in url:
            page_type = "about_page"

        elif ":" not in url:
            page_type = "record"

        else:
            page_type = "unknown type of page" + url
            print(page_type)

        # print(page_type)
        return page_type


# def return_links_within_div(url, div_name):
#     http = httplib2.Http()
#     status, response = http.request(url)

#     soup = BeautifulSoup(response, 'html.parser')

#     target_div = soup.find("div", id=div_name)

#     links = target_div.find_all('a')

#     list_links = []

#     for a in links:
#         link_relative = a.get("href")
#         link_absolute = urljoin(url, link_relative)
#         list_links.append(link_absolute)

#     return list_links

def return_links_within_div(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    target_divs = soup.find_all("div", class_="mw-content-ltr", id="mw-content-text")
    list_links = []

    for d in target_divs:
        links = d.find_all('a')



        for a in links:
            link_relative = a.get("href")
            link_absolute = urljoin(url, link_relative)
            list_links.append(link_absolute)


    if list_links != []:
        return list_links
    elif list_links == [] and isinstance(soup, BeautifulSoup):
        print("searched the page but did not find any relevant links")
        return "[]"
    else:
        print("error parsing page, probably never connected to the desired webpage")
        return "error parsing"

def links_with_connect_error(url):
    wait_seconds = 10
    amount_tries = 10

    links = None
    for i in range(amount_tries):
        try:
            with timeout(wait_seconds):
                links = return_links_within_div(url)

        except:
            print("can't connect")
    if links is None or links == "error parsing":
        print("tried to connectt: ", amount_tries, "for :", wait_seconds )

    else:
        return links


# def return_links_category(links_category=[], links_record=[]):
#     links_category = links_category
#     links_record = links_record

#     while links_category != []:
#         for l in links_category:
#             links = return_links_within_div(l)
#             links_category.remove(l)

#             for link in links:
#                 if type_page(link) == "category":
#                     links_category.append(link)

#                 elif type_page(link) == "record":
#                     links_record.append(link)

#         return_links_category(links_category, links_record)

#     return links_record

def return_links_category(links_category=[], links_record=[], category_visited=[], c=0):

#     print("starting links category")
#     print(links_category)

    links_category = links_category
    links_record = links_record
    category_visited = category_visited
    while links_category != []:
        c += 1
        print(c)
        for l in links_category:
            #links_with_connect_error
            #return_links_within_div
            links = links_with_connect_error(l)

            # print("Links: ", len(links))
#             print(links)
#             print("removing " + l)
            links_category.remove(l)
            category_visited.append(l)

#     return links_record
            count_records = 0
            count_categories = 0
            for link in links:
#                 print(link)
                type_p = type_page(link)
                if type_p == "category":

                    if (link not in category_visited) and (link not in links_category):
                        # print("adding category " + link)
                        links_category.append(link)
                        count_categories += 1
#                     print(link)

                elif type_p == "record":

                    if link not in links_record:

                        links_record.append(link)
                        count_records += 1
#                         print("adding record " + link)
#                     print(link)
                    else:
                        print("duplicate: ", link)

                else:
                    print("unknown type of page")
#                     print(type_p)
            # print("categories added: ", count_categories)
            # print("records added: ", count_records)
#         print("passing links record")
#         print(links_record)
        
#         print("passing links category")
#         print(links_category)
        return_links_category(links_category, links_record, category_visited, c)

    # if links_category == []:
    #     print("found that many links in the category and it's children: ", len(links_record))
    return links_record
