from bs4 import BeautifulSoup
import urllib.request
import re


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

