from bs4 import BeautifulSoup
import urllib.request
import re

import pandas as pd


def read_files(file_names, dir):
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


def readAll(list_link, acronyms_data_frame, df_index, verbose=False, require_acronym=True):

    for link in list_link:
        title, paragraph, wiki_record = get_paragraph_title_wikirec(link, verbose)

        if paragraph != None:

            series_acronym = getAcronymFromParapraph(title, paragraph, wiki_record, df_index, verbose)

            if verbose: print(series_acronym)

            if require_acronym:
                if series_acronym["akronim"] != "brak" and not (series_acronym["hasło_wikipedia"] == acronyms_data_frame["hasło_wikipedia"]).values.any():
                    acronyms_data_frame = acronyms_data_frame.append(series_acronym, ignore_index=True)

            else:
                acronyms_data_frame = acronyms_data_frame.append(series_acronym, ignore_index=True)

    return acronyms_data_frame


def get_paragraph_title_wikirec(url, verbose=False):

    paragraph = None

    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    wikiEnd = re.search(r'\/wiki\/.+', url)
    wikiEnd = wikiEnd.group()[6:]

    title = soup.find('h1')
    title = title.getText()
    # print(title)
    title = re.match(r'(\d|\w|\s|\-|\–)+', title)

    # print(title)

    title = title.group()

    # print(title[-1])
    if title[-1] == " ":
        title = title[0:-1]

    if verbose:
        print("Title: ", title, " Record: ", wikiEnd)

    paragraphs = soup.find_all('p')

    paragraph_main = ""

    print(title)
    # print(paragraphs)

    for p in paragraphs:
        b = p.find_all('b')
        if len(b) == 0:
            pass
            # print("length of b's equals 0")
        else:
            # print("length of b's does not equal 0")
            paragraph_main = p
            break

    # print(paragraph_main)



    if paragraph_main == "":
        return None, None, None

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


def get_acronym(paragraph):

    acronym = None

    acronym = re.search(r'\([A-Z][A-Z]+\s*\w*\s[A-Z]*', paragraph)

    if acronym is not None:
        acronym = acronym.group()

        if acronym[0:1] == "(":
            acronym = acronym[1:]

    if acronym is None:
        temp = re.search(r'\(([^\(|^\)])+\)', paragraph)

        if temp is not None:
            temp = temp.group()

            acronym = re.search(r'[A-Z][A-Z]+', temp)

            if acronym is not None:
                acronym = acronym.group()

            # if acronym[0:1] == "(":
            #     acronym = acronym[1:]




    if acronym is None:

        acronym = re.search(r'\,\s[A-Z][A-Z]+\s*\w*\s[A-Z]*', paragraph)

        if acronym is not None:
            acronym = acronym.group()

            if acronym[0:2] == ", ":
                acronym = acronym[2:]

    if acronym is None:
        acronym = "brak"
        # print(paragraph)


    return acronym


def get_translation_language(paragraph):

    latin_translation = None

    # łacina
    latin_translation = re.search(r'łac\.\s*(\w[a-z]+)(\w|\s)+', paragraph)
    english_translation = re.search(r'ang\.\s*(\w[a-z]+)(\-|\–|\w|\s)+', paragraph)


    if latin_translation is not None:
        latin_translation = latin_translation.group()
        translation = latin_translation[5:]
        language = latin_translation[0:4]

    elif english_translation is not None:
        english_translation = english_translation.group()
        translation = english_translation[5:]
        language = english_translation[0:4]


    if latin_translation is None and english_translation is None:
        translation = "brak"
        language = "brak"

    # matchObjTranslation = re.search(r'\(\w[a-z][a-z]..(\w|\s)+', paragraph)


#     if matchObjTranslation == None:
#         matchObjTranslation = re.search(r'\((\w|\s)+', paragraph)
# #     matchObjTranslation = re.search(r'\w\w\w.\xa0(\w|\s)+', text_work)

#
#     if matchObjTranslation == None:
#
#         print("no translation")
#         matchObjLanguage = "brak"
#         matchObjTranslationProper = "brak"
#
#     else:
# #         print("dupa")
# #         print(matchObjTranslation)
#
#         matchObjLanguage = re.search(r'\w+', matchObjTranslation.group())
# #         print(matchObjLanguage)
#         matchObjLanguage = matchObjLanguage.group()
#         matchObjTranslationProper = re.search(r'\s(\w|\s)+', matchObjTranslation.group())
#
# #         print(matchObjTranslationProper)
#         if matchObjTranslationProper == None:
#             matchObjTranslationProper = "brak"
#         else:
#             matchObjTranslationProper = matchObjTranslationProper.group()[1:]

    return translation, language


def getAcronymFromParapraph(title, paragraph, wiki_record, df_index, verbose):

    #     print(text_work)

    extension = re.match(r'(\w|\s|\-|\–)+', paragraph, re.UNICODE)

    extension = extension.group()

    if extension[-1] == " ":
        # print("space detected")

        extension = extension[0:-1]


    acronym = get_acronym(paragraph)


    translation, language = get_translation_language(paragraph)

    series_acronym = pd.Series([acronym, extension,
                                translation, language, wiki_record],
                                index=df_index)

    return series_acronym
