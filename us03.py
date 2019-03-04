'''
User Story 03
Birth before death
'''
from prettytable import PrettyTable
from datetime import datetime
import re
import readGed

                
def birthBeforeDeath(input):
    problem = False
    errors = []
    for i in input: 
        if i[3] != "NA":
            if i[6] != "NA":
                birthDate = datetime.strptime(i[3], '%Y-%m-%d')
                deathDate = datetime.strptime(i[6], '%Y-%m-%d') 
                if birthDate > deathDate:
                    errors.append("ERROR: INDIVIDUAL: US03: " + i[0] + ": Death date occurs before their date of birth.")
                    problem = True
    if problem == True: 
        for i in errors: 
            print(str(i))
    return errors

def main(lists): 
    birthBeforeDeath(lists)
