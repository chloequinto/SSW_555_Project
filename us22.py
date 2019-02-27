def uniqueIDs(input):
    indiIds = {}

    for i in input[0]:
        if i[0] not in indiIds:
            indiIds[i[0]] = 0
        indiIds[i[0]] += 1
    
    doubleKeyIndi = []
    
    for key, value in indiIds.items():
        if value > 1:
            doubleKeyIndi.append(key)
    
    for i in doubleKeyIndi:
        print(f"ERROR: INDIVIDUAL: US22: {i} is a duplicate key.")

    famIds = {}

    for i in input[1]:
        if i[0] not in famIds:
            famIds[i[0]] = 0
        famIds[i[0]] += 1
    
    doubleKeyFam = []
    
    for key, value in famIds.items():
        if value > 1:
            doubleKeyFam.append(key)
    
    for i in doubleKeyFam:
        print(f"ERROR: FAMILY: US22: {i} is a duplicate key.")
    
    return doubleKeyIndi, doubleKeyFam