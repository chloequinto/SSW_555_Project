'''
User Story 25
Unique first names in families

'''

def uniqueFirstNames(everything):
    # values hold list: name, lineNo
    famBirth = {}
    famNames = {}
    hasErrors = False

    for i, j in zip(everything[0], everything[2]):
        if i[7] != "NA":
            child = i[7].replace("{", "").replace("}", "").replace("'", "")
            if child not in famBirth:
                famBirth[child] = []
            famBirth[child].append([i[0], i[3], j[0]])
            if child not in famNames:
                famNames[child] = []
            famNames[child].append([i[0], i[1], j[0]])

    uniqueBirth = set()
    uniqueName = set()

    for key, value in famBirth.items():
        for i in value:
            if i[1] in uniqueBirth:
                print(f"ERROR: INDIVIDUAL: US25: {i[0]} has the same birthday as someone else on line {i[2]}")
                hasErrors = True
            else:
                uniqueBirth.add(i[1])
        uniqueBirth.clear()

    for key, value in famNames.items():
        for i in value:
            if i[1] in uniqueName:
                print(i)
                print(f"ERROR: INDIVIDUAL: US25: {i[0]} has the same name as someone else on line {i[2]}")
                hasErrors = True
            else:
                uniqueName.add(i[1])
        uniqueName.clear()
    
    return hasErrors