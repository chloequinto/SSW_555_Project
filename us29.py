'''
User Story 29
List all individual deaths

'''

from prettytable import PrettyTable

def deaths(input, lineNo):
    deaths = []
    for i, x in zip(input, lineNo):
        if i[6] != "NA":
            print("NOTE: US29: Individual " + i[0] + " on line " + str(x[0]) + " is dead.")
            deaths.append(i)
    
    return deaths