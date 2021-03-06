### Module imports ###
import os
import numpy as np
from random import randint
import json
import settings
import pickle
from fileProcess import FileReader, FileStore
from preProcessData import FeatureExtraction ,NLP
from pyvi import ViTokenizer
from sklearn.svm import LinearSVC
from gensim import corpora, matutils
from sklearn.metrics import classification_report
import argparse


### Global Variables ###


### Class declarations ###


### Function declarations ###
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'rb')   # return an open file handle


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ikjMatrix multiplication")
    parser.add_argument('-i', dest='filename', required=True,
                        help='File need predict', metavar='FILE',
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-m', dest='model', type=str, default='trained_model/logistic_model.pk', help='path to pretrained model')
    args = parser.parse_args()
    #  Read input data
    data = args.filename.read()

    if args.model == 'svm':
        classifier = pickle.load(open('trained_model/svm_model.pk', 'rb'))

    if args.model == 'knn':
        classifier = pickle.load(open('trained_model/knn_model_tfidf.pk', 'rb'))

    vectorizer = pickle.load(open(settings.VECTOR_EMBEDDING,'rb'))
    data_features = []
    data_features.append(' '.join(NLP(text=data.decode('utf-16le')).get_words_feature()))
    features = vectorizer.transform(data_features)

    # predict result 
    print(classifier.predict(features))
