"""
Create the topic models from the papers

 author: Dai Yao (dai@yaod.ai)
"""

import os, re, string
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel

from pprint import pprint

import pyLDAvis.gensim_models

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from textblob import Word

# number of topics to obtain
number_topics = 3

# configuration
FILE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(FILE_DIR))
# BASE_DIR = os.path.dirname(FILE_DIR)
_stop_word_file = os.path.join(BASE_DIR, "data/stopwords.en.txt")
_papers_folder = os.path.join(BASE_DIR, "data/papers/")

stop_words = []


def load_stopwords():
    with open(_stop_word_file, 'r', encoding='utf-8') as file:
        for line in file:
            if len(line.strip()) > 0 & (not line.startswith('#')):
                stop_words.append(line.strip())


load_stopwords()

pattern = r'[' + string.punctuation + '’\']'

papers = []
files = os.listdir(_papers_folder)
for file in files:
    with open(os.path.join(_papers_folder, file)) as f:
        paper = f.read().lower()
        paper = re.sub(pattern, '', paper)
        words = paper.split(' ')
        valid_words = [
            Word(word).singularize() for word in words
            if word not in stop_words and len(word.strip()) > 0]
        papers.append(valid_words)

id2word = Dictionary(papers)
corpus = [id2word.doc2bow(paper) for paper in papers]

lda_model = LdaModel(
    corpus=corpus,
    id2word=id2word,
    num_topics=number_topics,
    random_state=0,
    chunksize=100,
    alpha='auto',
    per_word_topics=True)

pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]

p = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)

# save the interactive html
pyLDAvis.save_html(p, os.path.join(BASE_DIR, 'vis/mksc_2022_topics_' + str(number_topics) + '.html'))
