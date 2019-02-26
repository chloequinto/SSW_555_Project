'''
User Story 16
All male members of family must have the same name

'''

from prettytable import PrettyTable

def sameLastName(inputs):
    males = {}
    # use family ids as key, add all men to list
    for i in inputs:
        if i[2] == "M":
            if i[8] != "NA":
                famId = i[8].replace("'", "").replace("{", "").replace("}", "")
                lastName = (i[1].split(" "))[1]
                if famId not in males:
                    males[famId] = []
                if lastName not in males[famId]:
                    males[famId].append(lastName)
            elif i[7] != "NA":
                famId = i[7].replace("'", "").replace("{", "").replace("}", "")
                lastName = (i[1].split(" "))[1]
                if famId not in males:
                    males[famId] = []
                if lastName not in males[famId]:
                    males[famId].append(lastName)

    # if there are different names, then the set should be greater than 1
    for i in males:
        if len(list(set(males[i]))) == 1:
            males[i] = True
        else:
            males[i] = False
    allSameName = []
    errors = []
    for i in inputs:

        spouse = i[8].replace("'", "").replace("{", "").replace("}", "")
        child = i[7].replace("'", "").replace("{", "").replace("}", "")
        if i[2] == "M":
            
            if spouse in males and not males[spouse]:
                print("ERROR: INDIVIDUAL: US16: " + i[1] + " does not have the same last name\n")
                errors.append("ERROR: INDIVIDUAL: US16: " + i[1] + " does not have the same last name")
            elif child in males and not males[child]:
                print("ERROR: INDIVIDUAL: US16: " + i[1] + " does not have the same last name\n")
                errors.append("ERROR: INDIVIDUAL: US16: " + i[1] + " does not have the same last name")
            else:
                allSameName.append(i)
    return allSameName, errors

def table(lists):
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
                     'Alive', 'Death', 'Child', 'Spouse']

    for i in lists[0]:
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
    # print("\nMale names")
    # print(x)

    # for i in lists[1]:
    #     print(i)

def main(lists):
    sameLastName(lists)