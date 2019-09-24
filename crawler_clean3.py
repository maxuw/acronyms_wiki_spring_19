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
              "goraczki_krwotoczne.txt", "grypa.txt", "choroby_pasorzytnicze.txt", 
              "choroby_przenoszone_drogą_płciową.txt", "kiła.txt", "choroby_przenoszone_przez_szczury.txt",
              "choroby_przenoszone_przez_owady.txt", "ATC-J04.txt", "gruźlica.txt", "choroby_bakteryjne.txt"]

crawler1 = Crawler()



links_from_files = crawler1.read_files(list_files, dir_)

# +
# links_from_files[1]
# -



df_index = ["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"]

acronyms_data_frame = pd.DataFrame(columns=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])

acronyms_data_frame

# +
# list_all_links
# -

acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=True, require_acronym=True)

# +
# acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=True)
# -



acronyms_data_frame



# +
# acronyms_data_frame.to_csv (r'medical_from_wiki.csv', index = None, header=True)
# -



link_opr = "https://pl.wikipedia.org/wiki/Zaka%C5%BCenia_opryszczkowe"

par1 = crawler1.getExtandParagraph(links_from_files[0][1], verbose=False)

par1 = crawler1.getExtandParagraph(link_opr, verbose=False)



crawler1.getAcronymFromParapraph(par1[0], par1[1], par1[2], df_index, verbose=False)

par1[1][0:-1]

par1 = crawler1.getExtandParagraph(links_from_files[0][1], verbose=False)

par1





wirusb = "Wirusowe zapalenie wątroby typu B (WZW typu B) – wirusowe zapalenie wątroby wywołane zakażeniem HBV występujące u człekokształtnych, dawniej określane mianem żółtaczki wszczepiennej. Choroba nadal powoduje epidemie w Azji i Afryce i jest endemiczna w Chinach oraz wielu innych częściach Azji. Około jednej trzeciej ludności świata zostało zainfekowanych wirusem zapalenia wątroby B[1], z czego 350 milionów to przewlekli nosiciele. Zakażenie HBV dotyka w Europie 1 na 50 osób[2]."

wzwb = "Wirus zapalenia wątroby typu B (WZW B, ang. hepatitis B virus, HBV) – otoczkowy wirus DNA z rodziny Hepadnaviridae, hepatotropowy i limfotropowy, powodujący wirusowe zapalenie wątroby typu B, zidentyfikowany przez Barucha Samuela Blumberga w 1967 roku[1]."

acronym = re.search(r'\([A-Z][A-Z]+\s*[A-Z]*', wirusb)

acronym.group()

pom = "Afrykański pomór świń (łac. Pestis africana suum; ang. African swine fever, ASF) – wirusowa, posocznicowa choroba świń o przebiegu ostrym lub przewlekłym. Cechą charakterystyczną jest bardzo silna wybroczynowość i bardzo wysoka śmiertelność."

acronym = re.search(r'\([^\(]+[A-Z][A-Z]+\s*\w*\s[A-Z]*', pom)

acronym = re.search(r'\(([^\(|^\)])+\)', pom)

acronym

acronym.group()

acr = acronym.group()

acr

acronym = re.search(r'[A-Z][A-Z]+', acr)

acronym



pom

latin_translation = re.search(r'łac\.(\w[a-z]+)(\w|\s)+', pom)

latin_translation = re.search(r'łac\.\s*(\w[a-z]+)(\w|\s)+', pom)

latin_translation



giano = "Zespół Gianottiego-Crostiego[1][2][3][4] in. choroba Gianottiego-Crostiego[5][6], ZGC (ang. Gianotti–Crosti syndrome, infantile papular acrodermatitis, papular acrodermatitis of childhood, papulovesicular acrolocated syndrome) – choroba dermatologiczna o podłożu wirusowym, o łagodnym przebiegu, charakteryzującą się czerwonomiedzianą symetryczną wysypką na policzkach, pośladkach oraz wyprostnych powierzchniach kończyn."

english_translation = re.search(r'ang\.\s*(\w[a-z]+)(\-|\–|\w|\s)+', giano)

english_translation

–
