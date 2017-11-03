#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:22:44 2017

@author: tusimple
"""

import numpy as np
import pandas as pd
from random import shuffle

def sgn(x):
    if x<=0:
        return -1
    return 1

filename = 'hw1_18_train.dat'
X = []
Y = []
with open(filename,'r') as f:
    for line in f:
        inList = line.split()
        curr = np.ones(5)
        curr[1] = float(inList[0])
        curr[2] = float(inList[1])
        curr[3] = float(inList[2])
        curr[4] = float(inList[3])
        X.append(curr)
        Y.append(float(inList[4]))

size = len(X)

search_lst = list(range(size))
counts = []

count = 0

w = np.zeros(5)
found = True
while found or count==50:
    shuffle(search_lst)
    found = False
    for i in search_lst:
        if sgn(np.dot(w,X[i]))!=Y[i]:
            w_new=w+wX[i]*Y[i]
            found = True
            count+=1
counts.append(count)

for run_iter in range(2000):
    count = 0
    shuffle(search_lst)
    w = np.zeros(5)
    found = True
    while found:
        found = False
        for i in search_lst:
            if sgn(np.dot(w,X[i]))!=Y[i]:
                w+=X[i]*Y[i]
                found = True
                count+=1
    counts.append(count)
print(sum(counts)/len(counts))
    