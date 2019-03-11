'''
    User Story 18
    Siblings should not marry
    
    '''
from prettytable import PrettyTable
from datetime import datetime
import re
import readGed

def return_marriages(input):
    problem = False
    fams = []
    marriage_pairs = []
    errors = []
    for i in input:
        if i[1] != "NA": # if married
            fams = []
            fams.append(i[3])
            fams.append(i[5])
            marriage_pairs.append(fams)

return marriage_pairs #returns pair of HusbID, WifeID

def return_children(input):
    problem = False
    fams = []
    children_list = []
    errors = []
    for i in input:
        if i[7:] != "NA": # if children exist
            fams = []
            fams.append(i[0])
            fams.append(i[7:])
            children_list.append(fams)

return children_list #returns famID and list of children

def siblingsCantMarry(input, marriage_pairs, children_list):
    errors = []
    husb_id = []
    wife_id = []
    problem = False
    #k[1] is an array of children
    for i in input:
        for j in marriage_pairs:
            for k in children_list:
                #if j[0:] in k[0:]: #if married pair in children
                #if marriage_pairs[0:] in children_list[1:]:
                #if any(match in marriage_pairs for match in children_list):
                #if j[0:] != "NA":
                if j[0] in k[1]:
                    if j[1] in k[1]:
                        errors.append("ERROR: FAMILY: US18: " + str(j) + " Siblings should not marry.")
                        problem = True

if problem == True:
    for i in errors:
        print(str(i))
    return errors


def main(input):
    return siblingsCantMarry(input, return_marriages(input), return_children(input))
