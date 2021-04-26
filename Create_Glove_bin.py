import argparse
import os
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors

# Create GloVe binary file
glove_file = os.path.join('C:/Users/haric/Google Drive/Try/ACS-QG/dataq/original/Glove/glove.840B.300d.txt')
tmp_file = get_tmpfile("glove.840B.300d.w2v.txt")
_ = glove2word2vec(glove_file, tmp_file)
model = KeyedVectors.load_word2vec_format(tmp_file)
model.save_word2vec_format('glove.840B.300d.bin', binary=True)