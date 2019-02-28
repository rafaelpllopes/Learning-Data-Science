# -*- coding: utf-8 -*-
"""Introdução a Data Science.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FlScuDfbSVfzkmNoaejJY9PCDhrXq44G
"""

import pandas as pd
notas = pd.read_csv('ratings.csv')
notas.head()

notas.shape

notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']
notas.head()

notas['nota'].unique()

notas['nota'].value_counts()

notas['nota'].mean()

notas.nota

notas.nota.head()

notas.nota.plot(kind='hist')

notas.nota.median()

notas.nota.describe()

!pip install seaborn==0.9.0
import seaborn as sns
sns.boxplot(notas.nota)

filmes = pd.read_csv('movies.csv')
filmes.columns = ["filmeId", "titulo", "generos"]
notas.query("filmeId==1").nota

"""Olhando os filmes"""

notas.query('filmeId==1').nota.mean()

notas.query('filmeId==2').nota.mean()

media_por_filme = notas.groupby('filmeId').nota.mean()
media_por_filme.head()

media_por_filme.plot(kind="hist")

sns.boxplot(media_por_filme)

media_por_filme.describe()

sns.distplot(media_por_filme)

sns.distplot(media_por_filme, bins=10)

import matplotlib.pyplot as plt
plt.hist(media_por_filme)
plt.title("Histograma das medias dos filmes")

tmdb = pd.read_csv('tmdb_5000_movies.csv')
tmdb.head()

tmdb.original_language.unique()

tmdb.groupby('original_language').original_language.count()

tmdb.vote_average.unique()

tmdb['original_language'].value_counts()

contagem_de_lingua = tmdb['original_language'].value_counts().to_frame().reset_index()
contagem_de_lingua.columns = ['original_lingua', 'total']
contagem_de_lingua.head()

sns.barplot(x="original_lingua", y="total", data = contagem_de_lingua)

sns.catplot(x = "original_language", kind='count', data = tmdb)

plt.pie(contagem_de_lingua["total"], labels = contagem_de_lingua['original_lingua']) #Não recomendado grafico de pizza ou torta

total_por_lingua = tmdb['original_language'].value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc['en']
total_do_resto = total_geral - total_de_ingles
print(total_de_ingles, total_do_resto)

dados = {
    "lingua" : ["ingles", "outros"],
    "total" : [total_de_ingles, total_do_resto]
}

dados = pd.DataFrame(dados)
dados

sns.barplot(x="lingua", y = "total", data=dados)

filmes_sem_lingua_original_em_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x = "original_language", kind="count", data = filmes_sem_lingua_original_em_ingles)

total_por_lingua_de_outros_filmes = tmdb.query("original_language != 'en'").original_language.value_counts()
total_por_lingua_de_outros_filmes

sns.catplot(x = "original_language", kind="count", data = filmes_sem_lingua_original_em_ingles, aspect = 2, order= total_por_lingua_de_outros_filmes.index)

sns.catplot(x = "original_language", kind="count", data = filmes_sem_lingua_original_em_ingles, aspect = 2, order= total_por_lingua_de_outros_filmes.index, palette="GnBu_d")

