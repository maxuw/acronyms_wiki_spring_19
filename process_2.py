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

# + pycharm={"is_executing": false}
import class_link_extractor

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
url = "https://pl.wikipedia.org/wiki/Kategoria:Choroby_wirusowe"

# + pycharm={"is_executing": false}
links = class_link_extractor.return_links_category([url])

# + pycharm={"is_executing": false}
links

# + pycharm={"is_executing": false}
import crawler

# + pycharm={"is_executing": false}
import pandas as pd

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
df_index = ["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"]

# + pycharm={"is_executing": false}
acronyms_data_frame = pd.DataFrame(columns=["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"])

# + pycharm={"is_executing": false}
acronyms_data_frame

# + pycharm={"is_executing": false}
url2 = "https://pl.wikipedia.org/wiki/Choroby_wirusowe"

# + pycharm={"is_executing": false}
crawler.get_paragraph_title_wikirec(url2, True)

# + pycharm={"is_executing": false}
acronyms_data_frame = crawler.readAll(links, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

# + pycharm={"is_executing": false}
# acronyms_data_frame = crawler1.readAll(links_from_files, acronyms_data_frame, df_index, verbose=True)
# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
acronyms_data_frame

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
# acronyms_data_frame.to_csv (r'medical_from_wiki.csv', index = None, header=True)
# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
list_files_2 = ["goraczki_krwotoczne.txt", "grypa.txt", "choroby_pasorzytnicze.txt", 
              "choroby_przenoszone_drogą_płciową.txt", "kiła.txt", "choroby_przenoszone_przez_szczury.txt",
              "choroby_przenoszone_przez_owady.txt", "ATC-J04.txt", "gruźlica.txt", "choroby_bakteryjne.txt"]

# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
links_from_files2 = crawler1.read_files(list_files_2, dir1)

# + pycharm={"is_executing": false}
links_from_files2[1]

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
acronyms_data_frame = crawler1.readAll(links_from_files2, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
acronyms_data_frame

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
list_files_3 = ["rikejstozy.txt", "choroby_grzybicze.txt", "pasażowalne_encefalopatie_gąbczaste.txt",  ]

# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
links_from_files3 = crawler1.read_files(list_files_3, dir1)

# + pycharm={"is_executing": false}
# links_from_files3[1]
# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
acronyms_data_frame = crawler1.readAll(links_from_files3, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

# + pycharm={"is_executing": false}
acronyms_data_frame

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
dir2 = "wiki_links/choroby_genetyczne/"

# + pycharm={"is_executing": false}
list_files_4 = ["choroby_genetyczne.txt"]

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
links_from_files4 = crawler1.read_files(list_files_4, dir2)

# + pycharm={"is_executing": false}
# links_from_files3[1]
# + pycharm={"is_executing": false}



# + pycharm={"is_executing": false}
acronyms_data_frame = crawler1.readAll(links_from_files4, acronyms_data_frame, df_index, verbose=False, require_acronym=True)

# + pycharm={"is_executing": false}
acronyms_data_frame

# + pycharm={"is_executing": false}


# + pycharm={"is_executing": false}
# acronyms_data_frame.to_csv (r'medical_from_wiki_3.csv', index = None, header=True)
# + pycharm={"is_executing": false}
("Antygen_HBs" == acronyms_data_frame["hasło_wikipedia"]).values.any()

# + pycharm={"is_executing": false}

