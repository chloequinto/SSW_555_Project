'''
User Story 16
All male members of family must have the same name

'''

from prettytable import PrettyTable

def sameLastName(inputs, lineNo):
    males = {}
    # check spouse and child indexes to get all family ids of the male members
    for i in inputs:
        if i[2] == "M":
            lastName = (i[1].split(" "))[1]
            if i[8] != "NA":
                famId = i[8].replace("'", "").replace("{", "").replace("}", "")
                if famId not in males:
                    males[famId] = []
                if lastName not in males[famId]:
                    males[famId].append(lastName)
            elif i[7] != "NA":
                famId = i[7].replace("'", "").replace("{", "").replace("}", "")
                if famId not in males:
                    males[famId] = []
                if lastName not in males[famId]:
                    males[famId].append(lastName)

    # if there are different names, then the set should be greater than 1
    for i, x in zip(males, lineNo):
        males[i] = True if len(list(set(males[i]))) == 1 else False

    allSameName = []
    errors = []
    for i in inputs:

        spouse = i[8].replace("'", "").replace("{", "").replace("}", "")
        child = i[7].replace("'", "").replace("{", "").replace("}", "")
        if i[2] == "M":
            
            if spouse in males and not males[spouse]:
                print(f"ERROR: INDIVIDUAL: US16: {i[1]} does not have the same last name on line {x[0]}")
                errors.append(f"ERROR: INDIVIDUAL: US16: {i[1]} does not have the same last name on line {x[0]}")
            elif child in males and not males[child]:
                print(f"ERROR: INDIVIDUAL: US16: {i[1]} does not have the same last name on line {x[0]}")
                errors.append(f"ERROR: INDIVIDUAL: US16: {i[1]} does not have the same last name on line {x[0]}")
            else:
                allSameName.append(i)
                
    return allSameName, errors