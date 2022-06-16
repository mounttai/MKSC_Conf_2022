"""
Extract all the papers from the text file

 author: Dai Yao (dai@yaod.ai)
"""

import string
import re

text_file = open("../data/mksc_conf_2022_paper_text.txt", 'r')

section_start_pattern = re.compile('^[T|F|S][A|B|C|D|E][0|1][1-9]')
paper_start_pattern = re.compile('^[1-8] -')

line_index = 0
paper_index = 1
paper_start = 0
page_file = None

while True:

    line_index = line_index + 1
    line = text_file.readline()

    if re.match(paper_start_pattern, line):
        paper_start = 1
        paper_file = open("../data/papers/paper_" + str(paper_index) + ".txt", 'w')
        paper_file.write(line.strip() + ' ')
        paper_index = paper_index + 1

    else:
        if re.match(section_start_pattern, line):
            paper_start = 0
            try:
                paper_file.close()
            except NameError:
                print("")

        '''only write the line if the paper is there'''
        print(str(line_index) + '\t' + str(paper_start) + '\t' + line)
        if paper_start == 1:
            paper_file.write(line.strip() + ' ')

    if not line:
        try:
            paper_file.close()
        except NameError:
            print("")

text_file.close()