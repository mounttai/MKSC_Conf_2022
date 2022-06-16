"""
Extract the text from the pdf files - note that there are two columns in the original .pdf file

 author: Dai Yao (dai@yaod.ai)
"""
import pdfplumber

paper_text_file = open("../data/mksc_conf_2022_paper_text.txt", 'w')

with pdfplumber.open("../data/298315070-2022_INFORMS_Marketing_Science_Program.pdf") as pdf:

    '''get the number of pages'''
    num_pages = len(pdf.pages)

    '''deal with each page'''
    for i in range(0, num_pages):
        print("page %s" % i)
        page = pdf.pages[i]

        '''each page has two columns - deal with the left column, then the right one'''
        left = page.crop((0, 0.1 * float(page.height), 0.5 * float(page.width), 0.95 * float(page.height)))
        right = page.crop((0.5 * float(page.width), 0.1 * float(page.height), page.width, 0.95 * float(page.height)))

        text = left.extract_text()
        paper_text_file.write(text + "\r\n")

        text = right.extract_text()
        paper_text_file.write(text + "\r\n")

paper_text_file.close()