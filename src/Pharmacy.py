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

def sort_dict(dictionary):
    unsorted_drugs = []
    for drug in dictionary:
        drug_attributes = [drug, dictionary[drug][0], len(dictionary[drug][1])]
        unsorted_drugs.append(drug_attributes)
    
    sorted_drugs = sorted(unsorted_drugs, 
                          key = lambda l: (l[1], l[0]), reverse = True)
    return sorted_drugs  

def write_output(sorted_list):
    output_file = open("../output/top_cost_drug.txt", "w+")
    output_file.write("drug_name,num_prescriber,total_cost\n")
    for drug in sorted_list:
        output_file.write("%s,%d,%d\n" % (drug[0], drug[2], drug[1]))
    output_file.close()
    
def make_dict(content):
    drug_dict = {}

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
            
    return drug_dict

input_file = open("../input/itcont.txt", "r")

content = input_file.readlines()

#Removing the header line
content.pop(0)

input_file.close()

unsorted_dict = make_dict(content)
sorted_list = sort_dict(unsorted_dict)
write_output(sorted_list)