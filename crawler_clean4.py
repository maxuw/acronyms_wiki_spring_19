# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.4
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



df_index = ["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"]

acronyms_data_frame = pd.DataFrame(columns=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])

acronyms_data_frame



dir1 = "wiki_links/choroby_zakaźne/"

list_files = ['wirusowe zapalenia watroby.txt', 'choroby_wirusowe.txt']

crawler1 = Crawler()



links_from_files = crawler1.read_files(list_files, dir1)

# +
# links_from_files[1]
# -
links_from_files


# +
# list_all_links
# -

acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

# +
# acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=True)
# -



acronyms_data_frame



# +
# acronyms_data_frame.to_csv (r'medical_from_wiki.csv', index = None, header=True)
# -










list_files_2 = ["goraczki_krwotoczne.txt", "grypa.txt", "choroby_pasorzytnicze.txt", 
              "choroby_przenoszone_drogą_płciową.txt", "kiła.txt", "choroby_przenoszone_przez_szczury.txt",
              "choroby_przenoszone_przez_owady.txt", "ATC-J04.txt", "gruźlica.txt", "choroby_bakteryjne.txt"]




links_from_files2 = crawler1.read_files(list_files_2, dir1)

links_from_files2[1]



acronyms_data_frame = crawler1.readAll(links_from_files2, acronyms_data_frame, df_index, verbose=False, require_acronym=True)



acronyms_data_frame







list_files_3 = ["rikejstozy.txt", "choroby_grzybicze.txt", "pasażowalne_encefalopatie_gąbczaste.txt",  ]




links_from_files3 = crawler1.read_files(list_files_3, dir1)

# +
# links_from_files3[1]
# -



acronyms_data_frame = crawler1.readAll(links_from_files3, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

acronyms_data_frame





dir2 = "wiki_links/choroby_genetyczne/"

list_files_4 = ["choroby_genetyczne.txt"]



links_from_files4 = crawler1.read_files(list_files_4, dir2)

# +
# links_from_files3[1]
# -



acronyms_data_frame = crawler1.readAll(links_from_files4, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

acronyms_data_frame



# +
# acronyms_data_frame.to_csv (r'medical_from_wiki_3.csv', index = None, header=True)
# -
("Antygen_HBs" == acronyms_data_frame["hasło_wikipedia"]).values.any()


