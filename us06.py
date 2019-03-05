'''
User Story 06
Divorce before death
'''
from prettytable import PrettyTable
from datetime import datetime
import re
import readGed

                
def indivDeaths(input):
    problem = False
    fams = []
    indivs = []
    errors = []
    for i in input: 
        if i[2] != "NA":
            fams = []
            fams.append(i[0])
            fams.append(i[2])
            fams.append(i[3])
            fams.append(i[5])
            indivs.append(fams)
            
    # print(indivs)        
    return indivs

def checkFams(input, indivs):
    errors = []
    problem = False
    for i in input:
        for j in indivs:
            if j[2] == i[0] or j[3] == i[0]: #checks 
                if i[6] != "NA": #if dead 
                    deathDate = datetime.strptime(i[6], '%Y-%m-%d')
                    divDate = datetime.strptime(j[1], '%Y-%m-%d') 
                    if divDate > deathDate:
                        errors.append("ERROR: INDIVIDUAL: US06: " + i[0] + ": Divorce date occurs after their date of death.")
                    problem = True

    if problem: 
        for i in errors: 
            print(i)
    return errors


def main(inputindi, inputfam):
    #indivDeaths(tables[1])
return checkFams(inputindi, indivDeaths(inputfam))