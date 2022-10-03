# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:07:40 2022

@author: Carrick
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

# The original train.json
df = pd.read_json(r".\data\train_orig.json", orient="records")

# df_test = pd.read_json(r".\data\test.json", orient="records")

def get_proauthors(row):
    return [i for i in row['authors'] if i < 100]

def get_coauthors(row):
    return [i for i in row['authors'] if i >= 100]

def has_proauthors(row):
    if len(row['proauthors']) > 0:
        return True
    else:
        return False


df['proauthors'] = df.apply(lambda row: get_proauthors(row), axis=1)
df['coauthors'] = df.apply(lambda row: get_coauthors(row), axis=1)

df['has_proauthors'] = df.apply(lambda row: has_proauthors(row), axis=1)

# df_f = df[df['has_proauthors']==False]

# df_t = df[df['has_proauthors']==True]

# df_f = resample(df_f, replace=True, n_samples=int(1/3 * len(df_t)), random_state=42)

# df = pd.concat([df_t, df_f])

df_train, df_valid, _, _ = train_test_split(df, df['has_proauthors'], stratify=df['has_proauthors'], test_size=0.2)

# df_train.drop(['has_proauthors'], axis=1).to_json(r".\data\downsamp\train.json", orient="records")
# df_valid.drop(['has_proauthors'], axis=1).to_json(r".\data\downsamp\valid.json", orient="records")

df_train.drop(['has_proauthors'], axis=1).to_json(r".\data\original\train.json", orient="records")
df_valid.drop(['has_proauthors'], axis=1).to_json(r".\data\original\valid.json", orient="records")

# df = pd.concat([df_train, df_test])
# df = pd.concat([df['abstract'], df['title']]).to_frame(name='text')
# df.to_json(r".\data\corpus.json", orient="records")