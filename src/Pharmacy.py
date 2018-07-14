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

file = open("../input/itcont.txt", "r")

content = file.readlines()

drug_dict = {}

#Removing the header line
content.pop(0)

for line in content:
    tokens = line.split(",")
    tokens[DRUG_COST_INDEX] = tokens[DRUG_COST_INDEX].strip()
    #drug_info = parse_entry(line)
    #if drug_info[0] not in drug_dict:
     #   drug_dict[drug_info[0]] = drug_info[1]
    #else:
     #   drug_dict[drug_info[0]] += drug_info[1]
        
