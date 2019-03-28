import sys
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn.externals import joblib
import nltk
from nltk import tokenize

if __name__ == "__main__":
    resenha = sys.argv[1]

    resenha = [resenha]
    regressao_logistica = joblib.load('/home/glauberc/Workspace/TCC/avaliacao-de-resenhas/python/regressaoModel.sav')
    vetorizar = joblib.load('/home/glauberc/Workspace/TCC/avaliacao-de-resenhas/python/vetorizarModel.sav')
    bag_of_words = vetorizar.transform(resenha)
    previsao = regressao_logistica.predict(bag_of_words)
    print(previsao)


    