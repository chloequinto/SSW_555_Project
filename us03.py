'''
User Story 03
Birth before death
'''
from prettytable import PrettyTable
from datetime import datetime
import re
import readGed


                
def birthBeforeDeath(input):
    errors = []
    for i in input: 
        if i[3] != "NA":
            if i[6] != "NA":
                try:
                    birthDate = datetime.strptime(i[3], '%Y-%m-%d')
                except ValueError:
                    birthDate = datetime.strptime("2018-01-01", '%Y-%m-%d')
                try:
                    deathDate = datetime.strptime(i[6], '%Y-%m-%d') 
                except ValueError:
                    deathDate = datetime.strptime("2018-01-01", '%Y-%m-%d') 
                
                if birthDate > deathDate:
                    errors.append("ERROR: INDIVIDUAL: US03: " + i[0] + ": Death date occurs before their date of birth.")
                    print("ERROR: INDIVIDUAL: US03: " + i[0] + ": Death date occurs before their date of birth.")
    
    return errors

def main(lists): 
    birthBeforeDeath(lists)
