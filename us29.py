'''
User Story 29
List all individual deaths

'''

from prettytable import PrettyTable

def deaths(input):
    deaths = []
    for i in input:
        if i[6] != "NA":
            print("NOTE: US29: Individual " + i[0] + " is dead.")
            deaths.append(i)
    
    return deaths