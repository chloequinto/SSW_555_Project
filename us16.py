from prettytable import PrettyTable

def sameLastName(inputs):
    males = {}
    # use family ids as key, add all last names to list
    # iterate over values, check if all are the same
    for i in inputs:
        if i[8] != "NA" and i[2] == "M":
            famId = i[8].replace("'", "").replace("{", "").replace("}", "")
            lastName = (i[1].split(" "))[1]
            if famId not in males:
                males[famId] = []
            males[famId].append(lastName)

    for i in males:
        if len(list(set(males[i]))) == 1:
            males[i] = True
    
    allSameName = []

    for i in inputs:
        famId = i[8].replace("'", "").replace("{", "").replace("}", "")
        if famId in males and males[famId] and i[2] == "M":
            allSameName.append(i)
    
    return allSameName

def table(lists): 
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
                     'Alive', 'Death', 'Child', 'Spouse']

    for i in lists:
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
    print("\nIndividuals")
    print(x)

def main(lists):
    table(sameLastName(lists))