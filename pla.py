#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:22:44 2017

@author: tusimple
"""

import numpy as np
import pandas as pd
from random import shuffle

def sgndot(w,x):
    if np.dot(w,x)<=0:
        return -1
    else:
        return 1

def read_data(filename):
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
    return X,Y

def betterThanPocket(X,Y,wn,wp):
    hitp = 0
    hitn = 0
    for i in range(len(X)):
        if sgndot(wp,X[i])==Y[i]:
            hitp += 1
        if sgndot(wn,X[i])==Y[i]:
            hitn += 1
#    print('hitp:'+str(hitp))
#    print('hitn:'+str(hitn))
    if hitn > hitp:
        return True
    return False
    

# 15.
ifUpdated = True
w = np.zeros(5)
X, Y = read_data('hw1_15_train.dat.txt')
m = len(X)
count = 0
while ifUpdated:
    ifUpdated = False
    for i in range(m):
        if sgndot(w,X[i])!=Y[i]:
            w += Y[i]*X[i]
            ifUpdated = True
            count += 1
print('updates #',count)
    
# 16.
X, Y = read_data('hw1_15_train.dat.txt')
m = len(X)
count_sum = 0
for j in range(2000):
    count = 0
    w = np.zeros(5)
    ifUpdated = True
    indlst = list(range(m))
    shuffle(indlst)
    while ifUpdated:
        ifUpdated = False
        for i in range(m):
            if sgndot(w,X[indlst[i]])!=Y[indlst[i]]:
                w += Y[indlst[i]]*X[indlst[i]]
                ifUpdated = True
                count += 1
    count_sum += count
print('avg updates #',count_sum/2000)
    
# 17.
X, Y = read_data('hw1_15_train.dat.txt')
m = len(X)
count_sum = 0
for j in range(2000):
    count = 0
    w = np.zeros(5)
    ifUpdated = True
    indlst = list(range(m))
    shuffle(indlst)
    while ifUpdated:
        ifUpdated = False
        for i in range(m):
            if sgndot(w,X[indlst[i]])!=Y[indlst[i]]:
                w += Y[indlst[i]]*X[indlst[i]]*0.5
                ifUpdated = True
                count += 1
    count_sum += count
print('avg updates #',count_sum/2000)


# 18.

def test(wp):
    Xt, Yt = read_data('hw1_18_test.dat.txt')
    err_hit = 0
    for i in range(len(Xt)):
        if sgndot(wp,Xt[i])!=Yt[i]:
            err_hit += 1
    return err_hit/len(Xt)

X, Y = read_data('hw1_18_train.dat.txt')
m = len(X)

err_sum = 0
for j in range(2000):
    w = np.zeros(5)
    wp = np.zeros(5)
    ifUpdated = True
    indlst = list(range(m))
    shuffle(indlst)
    count = 0
    while ifUpdated and  count < 50:
        ifUpdated = False
        for i in range(m):
            if sgndot(w,X[indlst[i]])!=Y[indlst[i]]:
                w += Y[indlst[i]]*X[indlst[i]]
                ifUpdated = True
                count += 1
                if betterThanPocket(X,Y,w,wp):
                    wp = w.copy()
    err_sum+=test(wp)
print('avg updates #',err_sum/2000)

# 19.

def test(wp):
    Xt, Yt = read_data('hw1_18_test.dat.txt')
    err_hit = 0
    for i in range(len(Xt)):
        if sgndot(wp,Xt[i])!=Yt[i]:
            err_hit += 1
    return err_hit/len(Xt)

X, Y = read_data('hw1_18_train.dat.txt')
m = len(X)

err_sum = 0
for j in range(2000):
    w = np.zeros(5)
    wp = np.zeros(5)
    ifUpdated = True
    indlst = list(range(m))
    shuffle(indlst)
    count = 0
    while ifUpdated and  count < 50:
        ifUpdated = False
        for i in range(m):
            if sgndot(w,X[indlst[i]])!=Y[indlst[i]]:
                w += Y[indlst[i]]*X[indlst[i]]
                ifUpdated = True
                count += 1
#                if betterThanPocket(X,Y,w,wp):
#                    wp = w.copy()
    err_sum+=test(w)
print('avg updates #',err_sum/2000)


# 20.

def test(wp):
    Xt, Yt = read_data('hw1_18_test.dat.txt')
    err_hit = 0
    for i in range(len(Xt)):
        if sgndot(wp,Xt[i])!=Yt[i]:
            err_hit += 1
    return err_hit/len(Xt)

X, Y = read_data('hw1_18_train.dat.txt')
m = len(X)

err_sum = 0
for j in range(2000):
    w = np.zeros(5)
    wp = np.zeros(5)
    ifUpdated = True
    indlst = list(range(m))
    shuffle(indlst)
    count = 0
    while ifUpdated and  count < 50:
        ifUpdated = False
        for i in range(m):
            if sgndot(w,X[indlst[i]])!=Y[indlst[i]]:
                w += Y[indlst[i]]*X[indlst[i]]
                ifUpdated = True
                count += 1
                if betterThanPocket(X,Y,w,wp):
                    wp = w.copy()
    err_sum+=test(wp)
print('avg updates #',err_sum/2000)