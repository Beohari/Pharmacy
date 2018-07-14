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
    # Strippnig the whitespace from the drug cost and casting to int
    tokens[DRUG_COST_INDEX] = int(tokens[DRUG_COST_INDEX].strip())
    drug_name = tokens[DRUG_INDEX]
    prescriber_name = (tokens[LAST_NAME_INDEX], tokens[FIRST_NAME_INDEX])
    
    if drug_name not in drug_dict:
        #For a new drug, we create an empty set and explicitly
        #add the prescriber name as a tuple
        drug_dict[drug_name] = [tokens[DRUG_COST_INDEX], set()]
        drug_dict[drug_name][1].add(prescriber_name)
    else:
        drug_dict[drug_name][0] += tokens[DRUG_COST_INDEX]
        drug_dict[drug_name][1].add(prescriber_name)