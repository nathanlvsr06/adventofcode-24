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

dist = []

while leftList != []:
    minLeftList = min(leftList)
    minRightList = min(rightList)
    dist.append(abs(minLeftList-minRightList))
    leftList.remove(minLeftList)
    rightList.remove(minRightList)

DISTANCE = sum(dist)

print("The total distance between the two lists is:", DISTANCE)