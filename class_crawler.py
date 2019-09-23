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
                title, paragraph, wiki_record = self.get_paragraph_title_wikirec(link, verbose)
                series_acronym = self.getAcronymFromParapraph(title, paragraph, wiki_record, df_index, verbose)
                if verbose: print(series_acronym)

                acronyms_data_frame = acronyms_data_frame.append(series_acronym, ignore_index=True)

        return acronyms_data_frame


    def get_paragraph_title_wikirec(self, url, verbose):

        paragraph = None

        page = urllib.request.urlopen(url)

        soup = BeautifulSoup(page, 'html.parser')

        wikiEnd = re.search(r'\/wiki\/.+', url)
        wikiEnd = wikiEnd.group()[6:]

        title = soup.find('h1')
        title = title.getText()
        # print(title)
        title = re.match(r'(\w|\s)+', title)

        # print(title)

        title = title.group()

        print(title[-1])
        if title[-1] == " ":
            title = title[0:-1]

        if verbose:
            print("Title: ", title, " Record: ", wikiEnd)

        paragraphs = soup.find_all('p')

        paragraph_main = ""

        for p in paragraphs:
            b = p.find_all('b')
            if len(b) == 0:
                print("length of b's equals 0")
            else:
                print("length of b's does not equal 0")
                paragraph_main = p
                break

        paragraph_main = paragraph_main.getText()

        # header_section = soup.find_all('p')


        #
        #
        #
        # for par in header_section:
        #     header_section_text = par.getText()
        #     if header_section_text[0:len(title)] == title:
        #         # print("title and par match")
        #
        #         paragraph = header_section_text
        #         break
        #
        # if paragraph is None:
        #     print("title and par DON'T match")
        #
        #     if len(header_section[0]) < 6:
        #         header_section = header_section[1]
        #
        #     else:
        #         header_section = header_section[0]
        #
        #     paragraph = header_section.getText()
        #
        #     print(title)
        #     print(paragraph)

        return title, paragraph_main, wikiEnd


    def getAcronymFromParapraph(self, title, paragraph, wiki_record, df_index, verbose):

        #     print(text_work)

        extension = re.match(r'(\w|\s)+', paragraph, re.UNICODE)

        extension = extension.group()

        if extension[-1] == " ":
            # print("space detected")

            extension = extension[0:-1]





        acronym = re.search(r'[A-Z][A-Z]+', paragraph) # ogranicz do pierwszego akapitu.

        if acronym == None:
            acronym = "brak"

        else:
            acronym = acronym.group()

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

        series_acronym = pd.Series([matchObjAcronym, extension,
                                    matchObjTranslationProper, matchObjLanguage, wiki_record],
                                   index=df_index)

        return series_acronym
