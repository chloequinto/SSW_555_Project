'''
US31 - Parents not too old
'''

# If family has children
# Store them to a list
# Get husband and wife id
# Store husband birthday
# store wife birthday
# iterate through children and compare birthdays

from prettytable import PrettyTable
from datetime import datetime
from datetime import timedelta
import readGed
import re

def checkForOldParents(inputIndi, inputFam, newFam):
    children = []
    fatherID = "None"
    motherID = "None"
    motherBirthday = "None"
    fatherBirthday = "None"
    errors = []
    Error = False
    
    for i in inputFam:
        if len(i) > 7:
            children = []
            #children.append(i[0])
            children.append(i[7:])
            motherID = i[5]
            fatherID = i[3]
            for j in inputIndi:
                if j[0] == fatherID and j[3] != "NA":
                    fatherBirthday = j[3]
                    fatherBirthDate = datetime.strptime(j[3], '%Y-%m-%d')
                    
                if j[0] == motherID and j[3] != "NA":
                    motherBirthday = j[3]
                    motherBirthDate = datetime.strptime(j[3], '%Y-%m-%d')
                    
            for k, b in zip(inputIndi, newFam):
                if k[0] in children[0] and k[3] != "NA":
                    childBirthday = k[3]
                    ChildBirthDate = datetime.strptime(k[3], '%Y-%m-%d')
                    if(ChildBirthDate > (fatherBirthDate+ timedelta(days=29200))):
                        print("Error: US12: Individual: " + k[0] + "'s father is too old on line: " + str(b[0]))
                        errors.append("Error: US12: Individual: " + k[0] + "'s father is too old on line: " + str(b[0]))
                        Error = True
                    if(ChildBirthDate > (motherBirthDate+ timedelta(days=21900))):
                        print("Error: US12: Individual: " + k[0] + "'s mother is too old on line: " + str(b[0]))
                        errors.append("Error: US12: Individual: " + k[0] + "'s mother is too old on line: " + str(b[0]))
                        Error = True
            return errors




def main(inputIndi, inputFam, newFam):
    checkForOldParents(inputIndi, inputFam, newFam)