# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:07:40 2022

@author: Carrick
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# The original train.json
df_train = pd.read_json(r".\data\papers.json", orient="records")

# df_test = pd.read_json(r".\data\test.json", orient="records")

# def get_proauthors(row):
#     return [i for i in row['authors'] if i < 100]

# def get_coauthors(row):
#     return [i for i in row['authors'] if i >= 100]

def has_proauthors(row):
    if len(row['proauthors']) > 0:
        return True
    else:
        return False


# df_train['proauthors'] = df_train.apply(lambda row: get_proauthors(row), axis=1)
# df_train['coauthors'] = df_train.apply(lambda row: get_coauthors(row), axis=1)
split_label = df_train.apply(lambda row: has_proauthors(row), axis=1)

df_train, df_valid, _, _ = train_test_split(df_train, split_label, stratify=split_label, test_size=0.2)

df_train.to_json(r".\data\train.json", orient="records")
df_valid.to_json(r".\data\valid.json", orient="records")

# df = pd.concat([df_train, df_test])
# df = pd.concat([df['abstract'], df['title']]).to_frame(name='text')
# df.to_json(r".\data\corpus.json", orient="records")