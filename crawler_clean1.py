# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from class_crawler import Crawler

# +
# importing libraries

from bs4 import BeautifulSoup
import urllib.request
import re
# -

import pandas as pd

dir_ = "wiki_links/"

list_files = ['wirusowe zapalenia watroby.txt', 'wirusowe_choroby_roslin.txt', 
              'choroby_wirusowe.txt', "goraczki_krwotoczne.txt", "grypa.txt", 
              "choroby_pasorzytnicze.txt"]

crawler1 = Crawler()



links_from_files = crawler1.read_files(list_files, dir_)

links_from_files[0][:5]



acronyms_data_frame = pd.DataFrame(columns=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])

acronyms_data_frame

# +
# list_all_links
# -



def readAll(lines_links, acronyms_data_frame):
    for linklist in lines_links:
        
        for link in linklist:
            link = link[:-1]
            series_acronym = getAcronymFromPage(link)
            print(series_acronym)
            acronyms_data_frame = acronyms_data_frame.append(series_acronym, ignore_index=True)
        
    return acronyms_data_frame


acronyms_data_frame = readAll(list_all_links, acronyms_data_frame)

acronyms_data_frame[0:10]

acronyms_data_frame.to_csv (r'medical_from_wiki.csv', index = None, header=True)





acronyms_data_frame


def getAcronymFromPage(url):
    
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    wikiEnd = re.search(r'\/wiki\/.+', url)
    wikiEnd = wikiEnd.group()[6:]

    header_section = soup.find_all('p')
    
    if len(header_section[0]) < 6:
        header_section = header_section[1]
        
    else:
        header_section = header_section[0]

    text_work = header_section.getText()

#     print(text_work)
    matchObjExtension = re.match(r'(\w|\s)+', text_work, re.UNICODE)


    matchObjAcronym = re.search(r'[A-Z][A-Z]+', text_work) # ogranicz do pierwszego akapitu.
    
    if matchObjAcronym == None:
        matchObjAcronym = "brak"
    
    else:
        matchObjAcronym = matchObjAcronym.group()

    matchObjTranslation = re.search(r'\(\w\w\w\..(\w|\s)+', text_work)
    
    if matchObjTranslation == None:
        matchObjTranslation = re.search(r'\((\w|\s)+', text_work)
#     matchObjTranslation = re.search(r'\w\w\w.\xa0(\w|\s)+', text_work)

    if matchObjTranslation == None:
        
        print("no translation")
        matchObjLanguage = "brak"
        matchObjTranslationProper = "brak"
        
        
    else:
#         print("dupa")
#         print(matchObjTranslation)

        matchObjLanguage = re.search(r'\w+', matchObjTranslation.group())
#         print(matchObjLanguage)
        matchObjLanguage = matchObjLanguage.group()
        matchObjTranslationProper = re.search(r'\s(\w|\s)+', matchObjTranslation.group())

#         print(matchObjTranslationProper)
        if matchObjTranslationProper == None:
            matchObjTranslationProper = "brak"
        else:
            matchObjTranslationProper = matchObjTranslationProper.group()[1:]
    
    series_acronym = pd.Series([matchObjAcronym, matchObjExtension.group(), 
                                matchObjTranslationProper, matchObjLanguage, wikiEnd], 
                               index=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])
    return series_acronym
    

series_acronym = getAcronymFromPage(url)

acronyms_data_frame.append(series_acronym, ignore_index=True)
