'''
User Story 28
Order siblings by age

'''

def orderSiblings(everyone):
    # values hold list: age, family the child is part of, lineNo
    individual = {}
    for i, x in zip(everyone[0], everyone[2]):
        if i[7] != "NA":
            if i[0] not in individual:
                child = i[7].replace("{", "").replace("}", "").replace("'", "")
                individual[i[0]] = []
            individual[i[0]] = [i[4], child, x[0]]
        
    # values hold list: individual, age, lineNo
    family = {}

    for indi, info in individual.items():
        if info[1] not in family:
            family[info[1]] = []
        family[info[1]].append([indi, info[0], info[2]])

    for key, value in family.items():
        value.sort(key = lambda x: x[1], reverse = True)
    
    print("NOTE: INDIVIDUAL: US28: Order Siblings by age")
    for key, value in family.items():
        # we only need families with more than one children
        if len(value) > 1:
            print(f"    Siblings by age for family {key}:")
            for i in value:
                print(f"        {i[0]}: Age {i[1]} on line {i[2]}")
    
    return family