'''
    User Story 18
    Siblings should not marry
    
'''

def return_marriages(input):
    fams = []
    marriage_pairs = []
    
    for i in input:
        if i[1] != "NA": # if married
            fams = []
            fams.append(i[3])
            fams.append(i[5])
            marriage_pairs.append(fams)

    return marriage_pairs #returns pair of HusbID, WifeID

def return_children(input):
    fams = []
    children_list = []
    
    for i in input:
        if i[7:] != "NA": # if children exist
            fams = []
            fams.append(i[0])
            fams.append(i[7:])
            children_list.append(fams)

    return children_list #returns famID and list of children

def siblingsCantMarry(marriage_pairs, children_list, lineNo):
    errors = []
    
    #k[1] is an array of children
    for j in marriage_pairs:
        for k, m in zip(children_list, lineNo):
            if j[0] in k[1] and j[1] in k[1]:
                print(f"ERROR: FAMILY: US18: {j} Siblings should not marry on line {m[0]}.")
                errors.append(f"ERROR: FAMILY: US18: {j} Siblings should not marry on line {m[0]}.")

    return errors


def main(input):
    return siblingsCantMarry(return_marriages(input[1]), return_children(input[1]), input[3])
