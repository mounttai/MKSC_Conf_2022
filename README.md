# MKSC_Conf_2022

The conference agenda is available at [this link](../../blob/main/data/298315070-2022_INFORMS_Marketing_Science_Program.pdf)

The following steps were taken to gain a quick understanding on topics presented in the conference:

* [extract_text_from_pdf.py](../../blob/main/code/extract_text_from_pdf.py) can extract the pure text from the above pdf file (it is a bit tricky as the pdf file has two columns);
* [extract_doc_from_text.py](../../blob/main/code/extract_doc_from_text.py) can separate the single text file created in the first step into single papers. **Altogether there are 556 presentations**;
* [create_topic_model_from_papers.py](../../blob/main/code/create_topic_model_from_papers.py) can create the topic distributions (for a given number) from all the papers;
* [create_topic_model_from_papers_on_topic.py](../../blob/main/code/create_topic_model_from_papers_on_topic.py) can create the topic distributions (for a given number) from all the papers **about a particular topic of interest**, e.g., live streaming.

A few observations could be made about the topics presented in the conference (using all the papers, and setting the number of topics as 10):

* the mainstream marketing topics still prevail, e.g. product, price, advertising, etc. (topic 1)
* social and content marketing keep emerging, the rise of influencer marketing and video marketing is noticeable (topic 2).
* diminishing interest in offline grocery shopping (topic 6)
* some interests in trendy topics, e.g., Covid (topic 7) and DEI (seemingly, topic 5).


**Topic 1** (based on all the papers and num-topics = 10)

![Topic 1](../../raw/main/vis/mksc-2022-topic-1.png?raw=true "Mainstream marketing topics on 4P")


**Topic 2** (based on all the papers and num-topics = 10)

![Topic 2](../../raw/main/vis/mksc-2022-topic-2.png?raw=true "Rising interest on social and content marketing")


**Topic 6** (based on all the papers and num-topics = 10)

![Topic 6](../../raw/main/vis/mksc-2022-topic-6.png?raw=true "Diminishing interest on offline grocery shopping")


**Topic 7** (based on all the papers and num-topics = 10)

![Topic 7](../../raw/main/vis/mksc-2022-topic-7.png?raw=true "Keen on mundane topic such as Covid")
