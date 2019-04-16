"""
US 24 - Unique Family by Spouses

No more than one family with the same spouses by name 
and the same marriage date should appear in a GEDCOM file
"""
import collections


def uniqueFam(family, line): 
    family_whole = []
    errors = []
    for i in family: 
        family_id = []
        family_id.append(i[1]) #marriage date 
        family_id.append(i[4]) #husband id
        family_id.append(i[6]) #wife id 
        family_whole.append(family_id) #whole id 
      
                
    first_tuple_list = [tuple(lst) for lst in family_whole]
    first_set = collections.OrderedDict.fromkeys(first_tuple_list)
    for i,b,c in zip(first_tuple_list, first_set, line):
        if b != i: 
            print("ERROR: FAMILY: US24: DUPLICATE FAMILY: " + c[1] + " WITH HUSBAND: " + i[1] + " AND WIFE " + i[2] + 
            " MARRIED ON " + i[0] + " on line " + str(c[0]))
            errors.append("ERROR: FAMILY: US24: DUPLICATE FAMILY: " + c[1] + " WITH HUSBAND: " + i[1] + " AND WIFE " + i[2] + 
            " MARRIED ON " + i[0] + " on line " + str(c[0]))
    return errors
                 


def main(familyLists, familyLine): 
    return uniqueFam(familyLists, familyLine)