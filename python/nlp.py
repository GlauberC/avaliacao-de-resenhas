# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn.externals import joblib
import nltk
from nltk import tokenize


def treinarModelo(): 
    
    
    
    resenha = pd.read_csv('../dados/filmes.csv')
    classificacao = resenha['sentiment'].replace(['neg', 'pos'],[0, 1])
    
    token_espaco = tokenize.WhitespaceTokenizer()
    palavras_irrelevantes = nltk.corpus.stopwords.words('portuguese')
    frase_processada = list()
    for opiniao in resenha['text_pt']:
        nova_frase = list()
        palavras_texto = token_espaco.tokenize(opiniao)
        for palavra in palavras_texto:
            if palavra not in palavras_irrelevantes:
                nova_frase.append(palavra)
        frase_processada.append(' '.join(nova_frase))
    resenha["tratamento_1"] = frase_processada
    
    
    resenha["classificacao"] = classificacao
    vetorizar = CountVectorizer(lowercase = False, max_features = 200)
    bag_of_words = vetorizar.fit_transform(resenha['tratamento_1'])
    treino, teste, classe_treino, classe_teste = train_test_split(bag_of_words, 
                                                                  resenha['classificacao'],
                                                                 random_state = 42)
    regressao_logistica = LogisticRegression( solver = 'lbfgs')
    regressao_logistica.fit(treino, classe_treino)
    
    filenameReg = 'regressaoModel.sav'
    joblib.dump(regressao_logistica, filenameReg)

    filenameVet = 'vetorizarModel.sav'
    joblib.dump(vetorizar, filenameVet)
    