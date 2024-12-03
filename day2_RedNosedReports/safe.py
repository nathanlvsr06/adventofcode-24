# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 02:27:22 2024

@author: nathanlvsr06
"""

def isIncreasing(L: list) -> bool:
    '''
    Entrée:
        - L, list
    Sortie:
        -  , bool
    Renvoie True si la liste est croissante, False sinon
    '''
    n = len(L)
    for i in range(n-1):
        if L[i+1] <= L[i]:
            return False
    return True

def isDecreasing(L: list) -> bool:
    '''
    Entrée:
        - L, list
    Sortie:
        - res, bool
    Renvoie True si la liste est décroissante, False sinon
    '''
    n = len(L)
    for i in range(n-1):
        if L[i+1] >= L[i]:
            return False
    return True

def isExcessive(L: list) -> bool:
    '''
    Entrées:
        - L, list
    Sortie:
        - , bool
    Renvoie True si la liste est excessive, False sinon
    '''
    n = len(L)
    for i in range(n-1):
        if  abs(L[i] - L[i+1]) <= 1 or  abs(L[i] - L[i+1]) >= 3:
            return False
    return True

def isSafe(L: list) -> bool:
    '''
    Entrées:
        - L, list
    Sortie:
        - res, bool
    Renvoie True si la liste est "safe", False sinon
    '''
    res = False
    if (isDecreasing(L) or isIncreasing(L)) and not isExcessive(L):
        res = True
    return res