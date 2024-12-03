# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:00:00 2024

@author: nathanlvsr06
"""

leftList = []
rightList = []

with open("input.txt", "r") as file:
    for line in file:
        leftList.append(int(line[:5]))
        rightList.append(int(line[8:]))

'''Part One'''


dist = []

while leftList != []:
    minLeftList = min(leftList)
    minRightList = min(rightList)
    dist.append(abs(minLeftList-minRightList))
    leftList.remove(minLeftList)
    rightList.remove(minRightList)

DISTANCE = sum(dist)

print("The total distance between the two lists is:", DISTANCE)


'''Part Two'''

with open("input.txt", "r") as file:
    for line in file:
        leftList.append(int(line[:5]))
        rightList.append(int(line[8:]))

def similarity(L1: list, L2: list) -> float:
    '''
    Entrées:
        - L1, list: première liste
        - L2, list: deuxième liste
    Sortie:
        - sim, float: similitude entre les deux listes
    '''
    sim = 0
    for number in L1:
        sim += number*L2.count(number)
    return sim

SIMILARITY = similarity(leftList, rightList)
print("Their similarity score is:", SIMILARITY)