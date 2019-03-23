'''
User Story 04
Marriage before divorce
'''
from prettytable import PrettyTable
from datetime import datetime
import re
import readGed

                
def marriageBeforeDivorce(input):
    problem = False
    errors = []
    for j in input: 
        if j[1] != "NA":
            if j[2] != "NA":
                marriageDate = datetime.strptime(j[1], '%Y-%m-%d')
                divorceDate = datetime.strptime(j[2], '%Y-%m-%d')
                if marriageDate > divorceDate:
                    errors.append("ERROR: FAMILY: US04: " + j[0] + ": Divorce date occurs before their marriage.")
                    problem = True
    if problem == True: 
        for i in errors: 
            print(str(i))
    return errors

def main(lists):
    marriageBeforeDivorce(lists)