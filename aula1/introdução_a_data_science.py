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

import seaborn as sns
sns.boxplot(notas.nota)



