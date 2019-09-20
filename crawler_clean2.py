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



df_index = ["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"]

acronyms_data_frame = pd.DataFrame(columns=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])

acronyms_data_frame

# +
# list_all_links
# -



# +
#acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=False)
# -



acronyms_data_frame[0:10]



acronyms_data_frame.to_csv (r'medical_from_wiki.csv', index = None, header=True)





par1 = crawler1.getParagraph(links_from_files[0][1], verbose=False)

par1

crawler1.getAcronymFromParapraph(par1[0], par1[1], df_index, verbose=False)

par1[1][0:-1]


