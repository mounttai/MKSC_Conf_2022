# MKSC_Conf_2022

The conference agenda is available at [this place](../../raw/main/data/298315070-2022_INFORMS_Marketing_Science_Program.pdf)

The following steps were taken to gain a quick opinions on topics presented in the conference:

* extract_text_from_pdf.py can extract the pure text from the above pdf file (it is a bit tricky as the pdf file has two columns);
* extract_doc_from_text.py can separate the single text file created in the first step into single papers. Altogether there are 533 presentations;
* create_topic_from_papers.py can create the topic distributions (for a given number) from all the papers;
* create_topic_from_papers_on_topic.py can create the topic distributions (for a given number) from all the papers about a particular topic of interest, e.g., live streaming.

A few observations could be made about the topics presented in the conference (using all the papers, and setting the number of topics as 10):

* the mainstream marketing topics still prevail, e.g. product, price, advertising, etc. (topic 1)
* social and content marketing keep emerging, the rise of influencer marketing and video marketing is noticeable (topic 2).
* diminishing interest in offline grocery shopping (topic 6)
* some interests in trendy topics, e.g., Covid (topic 7) and DEI (seemingly topic 5).


Topic 1 (based on all the papers and num-topics = 10)

![Topic 1](../../raw/main/vis/mksc-2022-topic-1.png?raw=true "Mainstream marketing topics on 4P")
