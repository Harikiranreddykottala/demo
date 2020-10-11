# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:04:30 2020

@author: khkre
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("D:\election.csv")
df.info()
df.describe()
df.isnull().sum()
df.dropna(axis=0,inplace=True)
df.columns=df.columns.str.replace('\n','')
df.columns
'''['STATE', 'CONSTITUENCY', 'NAME', 'WINNER', 'PARTY', 'SYMBOL', 'GENDER',
       'CRIMINALCASES', 'AGE', 'CATEGORY', 'EDUCATION', 'ASSETS',
       'LIABILITIES', 'GENERALVOTES', 'POSTALVOTES', 'TOTALVOTES',
       'OVER TOTAL ELECTORS IN CONSTITUENCY',
       'OVER TOTAL VOTES POLLED IN CONSTITUENCY', 'TOTAL ELECTORS']'''
Total_seats=df.CONSTITUENCY.nunique()
state_wise_seats=(df[df.WINNER==1]['STATE']).value_counts()
(df[df.WINNER==1]['STATE']).value_counts().head(15).plot(kind='bar')
party_wise_contested=df.PARTY.value_counts()
df.PARTY.value_counts().head(15).plot(kind='bar')
party_wise_won=(df[df.WINNER==1]['PARTY']).value_counts()
(df[df.WINNER==1]['PARTY']).value_counts().head(10).plot(kind='bar')

won_candidates=df[df.WINNER==1]
state_wise_party=won_candidates.groupby('STATE')['PARTY'].value_counts()
won_candidates.groupby('STATE')['PARTY'].value_counts().head(20).plot(kind='bar')
