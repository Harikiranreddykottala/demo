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