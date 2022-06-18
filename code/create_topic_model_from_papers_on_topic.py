"""
Create the topic models from the papers about a certain topic, e.g., live streaming, or privacy

define two new variables:
- topic_name (see below) - a brief name of the topic
- topic related keywords - a set of words that are used to search the corpus

 author: Dai Yao (dai@yaod.ai)
"""
import os, re, string
from pprint import pprint
from textblob import Word
import shutil
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel
import pyLDAvis.gensim_models

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

topic_name = "streaming"
topic_related_keywords = ['live', 'streaming', 'livestreaming', 'livestream', 'influencer']

topic_name = "privacy"
topic_related_keywords = ['privacy', 'sensitive', 'secret', 'intimate']

topic_name = "covid19"
topic_related_keywords = ['covid', 'covid19', 'pandemic', 'intimate', 'health', 'healthcare']

# number of topics to obtain
number_topics = 3

# configuration
FILE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(FILE_DIR))
# BASE_DIR = os.path.dirname(FILE_DIR)
_stop_word_file = os.path.join(BASE_DIR, "data/stopwords.en.txt")
_papers_folder = os.path.join(BASE_DIR, "data/papers/")
# additional configuration about a particular topic
_topic_papers_folder = os.path.join(BASE_DIR, "data/papers_"+topic_name+"/")
if not os.path.exists(_topic_papers_folder):
    os.mkdir(_topic_papers_folder)


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
indices = []
for file in files:
    with open(os.path.join(_papers_folder, file)) as f:
        paper = f.read().lower()
        paper = re.sub(pattern, '', paper)
        words = paper.split(' ')
        valid_words = [
            Word(word).singularize() for word in words
            if word not in stop_words and len(word.strip()) > 0]

        # include only if valid_words contain any in the keyword set
        if len(list(set(topic_related_keywords) & set(valid_words))) > 0:
            valid_words = [word for word in valid_words if word not in topic_related_keywords]
            papers.append(valid_words)
            # add the file
            indices.append(file)
            shutil.copy2(os.path.join(_papers_folder, file), os.path.join(_topic_papers_folder, file))

id2word = Dictionary(papers)
corpus = [id2word.doc2bow(paper) for paper in papers]

# run topic-modeling
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
pyLDAvis.save_html(p, os.path.join(BASE_DIR, 'vis/'+topic_name+'_topics_' + str(number_topics) + '.html'))

# output some stats
print("# of papers about live streaming: " + str(len(papers)))
indices.sort()
print('\n'.join('{}: {}'.format(*k) for k in enumerate(indices)))
