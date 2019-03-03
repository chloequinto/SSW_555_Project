'''
User Story 26
Corresponding entries

'''

from collections import OrderedDict

def corrEntries(input):
    addIndiIdsToFam = {}

    # check famIds for each individual and pulls indivdual ID
    for i in input[0]:
        if i[8] != "NA":
            temp = i[8].replace("{", "").replace("}", "").replace("'", "")
            if temp not in addIndiIdsToFam:
                addIndiIdsToFam[temp] = []
            addIndiIdsToFam[temp].append(i[0])
        if i[7] != "NA":
            temp = i[7].replace("{", "").replace("}", "").replace("'", "")
            if temp not in addIndiIdsToFam:
                addIndiIdsToFam[temp] = []
            addIndiIdsToFam[temp].append(i[0])
    
    famIdWithAllIndiID = {}

    for i in input[1]:
        if i[0] not in famIdWithAllIndiID:
            famIdWithAllIndiID[i[0]] = []
        if i[3] != "NA":
            famIdWithAllIndiID[i[0]].append(i[3])
        if i[5] != "NA":
            famIdWithAllIndiID[i[0]].append(i[5])
        if (len(i[7:]) > 0):
            temp = i[7].replace("{", "").replace("}", "").replace("'", "").split(",")
            for j in temp:
                famIdWithAllIndiID[i[0]].append(j)
        
    indiIdSorted = OrderedDict(sorted(addIndiIdsToFam.items()))
    famIdSorted = OrderedDict(sorted(famIdWithAllIndiID.items()))
    errors = []

    for (key, value), (key1, value1) in zip(indiIdSorted.items(), famIdSorted.items()):
        value.sort()
        value1.sort()
        if value != value1:
            errors.append(f"ERROR: FAMILY: US26: Family {key} does not have the correct corresponding entries")
            print(f"ERROR: FAMILY: US26: Family {key} does not have the correct corresponding entries")
    
    return errors