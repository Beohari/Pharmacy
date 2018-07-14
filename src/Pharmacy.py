# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 13:52:14 2018

@author: Ian
"""

ID_INDEX = 0
LAST_NAME_INDEX = 1
FIRST_NAME_INDEX = 2
DRUG_INDEX = 3
DRUG_COST_INDEX = 4

def parse_entry (line):
    tokens = line.split(",")
    drug = tokens[DRUG_INDEX]
    #Stripping the newline character
    drug_cost = int(tokens[DRUG_COST_INDEX].strip())
    return [drug, drug_cost]

file = open("../input/itcont.txt", "r")

content = file.readlines()

#Removing the header line
content.pop(0)

for line in content:
    drug_info = parse_entry(line)
    print(drug_info[1])