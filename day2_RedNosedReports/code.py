# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 02:08:50 2024

@author: nathanlvsr06
"""

from safe import isSafe

with open("input.txt", 'r') as file:
            lines = file.readlines()
            
            data = []
            for line in lines:
                report = line.strip().split()
                data.append([int(val) for val in report])


numSafe = 0
for report in data:
        if isSafe(report):
                numSafe += 1

print(numSafe,"reports are safe.")



        


