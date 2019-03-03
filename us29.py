'''
User Story 29
List all individual deaths

'''

from prettytable import PrettyTable

def deaths(input):
    deaths = []
    for i in input:
        if i[6] != "NA":
            print("Individual " + i[0] + " is dead.")
            deaths.append(i)
    
    return deaths