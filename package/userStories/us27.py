'''
US27
List all individuals and their age

'''

def listPeopleAndAge(people, lineNos):
    for i, j in zip(people, lineNos):
        print(f"NOTE: INDIVIDUAL: US27: Individual {i[0]} is {i[4]} years old on line {j[0]}")