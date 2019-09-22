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

list_files = ['wirusowe zapalenia watroby.txt', 'choroby_wirusowe.txt', 
              "goraczki_krwotoczne.txt", "grypa.txt", "choroby_pasorzytnicze.txt"]

crawler1 = Crawler()



links_from_files = crawler1.read_files(list_files, dir_)

links_from_files[1]



df_index = ["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"]

acronyms_data_frame = pd.DataFrame(columns=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])

acronyms_data_frame

# +
# list_all_links
# -



acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=True)



acronyms_data_frame[0:10]



# +
# acronyms_data_frame.to_csv (r'medical_from_wiki.csv', index = None, header=True)
# -





par1 = crawler1.getExtandParagraph(links_from_files[0][1], verbose=False)

par1

crawler1.getAcronymFromParapraph(par1[0], par1[1], par1[2], df_index, verbose=False)

par1[1][0:-1]

par1 = crawler1.getExtandParagraph(links_from_files[0][1], verbose=False)

par1



# +
page = urllib.request.urlopen(links_from_files[0][1])

soup = BeautifulSoup(page, 'html.parser')

# +
# paragraphs = soup.find_all('p')
# paragraphs
# -

paragraphs = soup.find_all('p')
paragraphs

# +
# par = t.find_all('b')

paragraph_main = ""

for p in paragraphs:
    b = p.find_all('b')
    if len(b) == 0:
        print("length of b's equals 0")
    else:
        print("length of b's does not equal 0")
        paragraph_main = p
        break

# -

paragraph_main

        for b_ in b:
        
            b_ = b_.getText()
            print(b_)
#         if b_ == "":
#             print("empty string")
#         print(len(b_))




