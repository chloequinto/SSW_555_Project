'''
User Story 22
Unique IDs for families and individuals

'''
def uniqueIDs(input):
    indiIds = {}
    lineNo = []

    for i, x in zip(input[0], input[2]):
        if i[0] not in indiIds:
            indiIds[i[0]] = 0
        indiIds[i[0]] += 1
        lineNo.append(x[0])
    
    doubleKeyIndi = []
    
    for (key, value), x in zip(indiIds.items(), lineNo):
        if value > 1:
            print(f"ERROR: INDIVIDUAL: US22: {key} is a duplicate key on line {x}")
            doubleKeyIndi.append(key)

    famIds = {}

    for i in input[1]:
        if i[0] not in famIds:
            famIds[i[0]] = 0
        famIds[i[0]] += 1
    
    doubleKeyFam = []
    
    for (key, value), x in zip(famIds.items(), lineNo):
        if value > 1:
            print(f"ERROR: FAMILY: US22: {key} is a duplicate key on line {x}")
            doubleKeyFam.append(key)
    
    return doubleKeyIndi, doubleKeyFam