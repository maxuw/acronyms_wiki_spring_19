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

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
import link_extractor

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
import crawler

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
import pandas as pd

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}



# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
url = "https://pl.wikipedia.org/wiki/Kategoria:Choroby_wirusowe"

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
links = link_extractor.return_links_category([url])

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
links

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}



# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
acronyms_data_frame

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}



# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
list_records = crawler.readAll(links, verbose=False, require_acronym=True)
# -


list_records



# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
acronyms_data_frame = crawler.readAll(links, acronyms_data_frame, df_index, verbose=False, require_acronym=True)
# -





# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
df_index = ["akronim", "fraza polska", "fraza obca", "język", "hasło_wikipedia"]

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
acronyms_data_frame = pd.DataFrame(list_records, columns=df_index)
# -

acronyms_data_frame

# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}



# + jupyter={"outputs_hidden": false} pycharm={"name": "#%%\n"}
acronyms_data_frame.to_csv (r'result.csv', index = None, header=True)
# -


