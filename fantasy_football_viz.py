# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:13:31 2021

@author: Jesse
"""

import pandas as pd
#load all the files in and create position varaible for all
qb = pd.read_csv("qbs.txt", sep="\t")
qb["pos"] = "QB"

rb = pd.read_csv("rbs.txt", sep="\t")
rb["pos"] = "RB"

wr = pd.read_csv("wr.txt", sep="\t")
wr["pos"] = "WR"

te = pd.read_csv("te.txt", sep="\t")
te["pos"] = "TE"
#create one big file
df = qb.append(rb)
df = df.append(wr)
df = df.append(te)
df = df.reset_index()

df = df.drop(["index"], axis=1)
df.head()
