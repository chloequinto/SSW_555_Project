'''
User Story 03
Birth before death
'''
from datetime import datetime


                
def birthBeforeDeath(input, lineNum):
    errors = []
    for i, x in zip(input, lineNum): 
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
                    errors.append(f"ERROR: INDIVIDUAL: US03: {i[0]} on line: {x[0]}: Death date occurs before their date of birth.")
                    print(f"ERROR: INDIVIDUAL: US03: {i[0]} on line: {x[0]}: Death date occurs before their date of birth.")
    
    return errors

def main(lists, lineNum): 
    birthBeforeDeath(lists, lineNum)
