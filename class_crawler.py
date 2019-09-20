from bs4 import BeautifulSoup
import urllib.request
import re

import pandas as pd

class Crawler:


    def read_files(self, file_names, dir):
        final_list = []

        for file in file_names:
            # Open the file with read only permit
            f = open(dir + file, "r")
            # use readlines to read all lines in the file
            # The variable "lines" is a list containing all lines in the file
            lines = f.readlines()
            # close the file after reading the lines.
            f.close()
            final_list.append(lines)

        return final_list


    def readAll(self, nested_links, acronyms_data_frame, df_index, verbose):
        for list_link in nested_links:

            for link in list_link:
                link = link[:-1]
                paragraph, wiki_end = self.getParagraph(link, verbose)
                series_acronym = self.getAcronymFromParapraph(paragraph, wiki_end, df_index, verbose)
                if verbose: print(series_acronym)

                acronyms_data_frame = acronyms_data_frame.append(series_acronym, ignore_index=True)

        return acronyms_data_frame


    def getParagraph(self, url, verbose):

        page = urllib.request.urlopen(url)

        soup = BeautifulSoup(page, 'html.parser')

        wikiEnd = re.search(r'\/wiki\/.+', url)
        wikiEnd = wikiEnd.group()[6:]

        header_section = soup.find_all('p')

        if len(header_section[0]) < 6:
            header_section = header_section[1]

        else:
            header_section = header_section[0]

        paragraph = header_section.getText()

        return paragraph, wikiEnd


    def getAcronymFromParapraph(self, paragraph, wiki_end, df_index, verbose):

    #     print(text_work)
        matchObjExtension = re.match(r'(\w|\s)+', paragraph, re.UNICODE)

        matchObjExtension = matchObjExtension.group()

        if matchObjExtension[-1] == " ":
            # print("space detected")

            matchObjExtension = matchObjExtension[0:-1]



        matchObjAcronym = re.search(r'[A-Z][A-Z]+', paragraph) # ogranicz do pierwszego akapitu.

        if matchObjAcronym == None:
            matchObjAcronym = "brak"

        else:
            matchObjAcronym = matchObjAcronym.group()

        matchObjTranslation = re.search(r'\(\w[a-z][a-z]..(\w|\s)+', paragraph)

    #     if matchObjTranslation == None:
    #         matchObjTranslation = re.search(r'\((\w|\s)+', paragraph)
    # #     matchObjTranslation = re.search(r'\w\w\w.\xa0(\w|\s)+', text_work)

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

        series_acronym = pd.Series([matchObjAcronym, matchObjExtension,
                                    matchObjTranslationProper, matchObjLanguage, wiki_end],
                                   index=df_index)
        return series_acronym


