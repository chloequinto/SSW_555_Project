'''
User Story 26
Corresponding entries

'''

from collections import OrderedDict

def corrEntries(everything):
    addIndiIdsToFam = {}

    # check famIds for each individual and pulls indivdual ID
    for i, x in zip(everything[0], everything[2]):
        if i[8] != "NA":
            temp = i[8].replace("{", "").replace("}", "").replace("'", "")
            if temp not in addIndiIdsToFam:
                addIndiIdsToFam[temp] = []
            addIndiIdsToFam[temp].append([i[0], x[0]])
        if i[7] != "NA":
            temp = i[7].replace("{", "").replace("}", "").replace("'", "")
            if temp not in addIndiIdsToFam:
                addIndiIdsToFam[temp] = []
            addIndiIdsToFam[temp].append([i[0], x[0]])
    
    famIdWithAllIndiID = {}

    for i, x in zip(everything[1], everything[3]):
        if i[0] not in famIdWithAllIndiID:
            famIdWithAllIndiID[i[0]] = []
        if i[3] != "NA":
            famIdWithAllIndiID[i[0]].append([i[3], x[0]])
        if i[5] != "NA":
            famIdWithAllIndiID[i[0]].append([i[5], x[0]])
        if (len(i[7:]) > 0):
            temp = i[7].replace("{", "").replace("}", "").replace("'", "").split(",")
            for j in temp:
                famIdWithAllIndiID[i[0]].append([j, x[0]])
        
    indiIdSorted = OrderedDict(sorted(addIndiIdsToFam.items()))
    famIdSorted = OrderedDict(sorted(famIdWithAllIndiID.items()))
    errors = []

    for (key, value), (key1, value1) in zip(indiIdSorted.items(), famIdSorted.items()):
        if value[0][0] != value1[0][0]:
            errors.append(f"ERROR: FAMILY: US26: Family {key} does not have the correct corresponding entries on line {value1[0][1]}")
            print(f"ERROR: FAMILY: US26: Family {key} does not have the correct corresponding entries on line {value1[0][1]}")
    
    return errors