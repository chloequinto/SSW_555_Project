'''
User Story 36
List recent deaths
'''
from prettytable import PrettyTable
import re
from datetime import date
from datetime import datetime,timedelta
import readGed

def recentDeaths(input):
    problem = False
    errors = []
    for x in input: 
        if x[7] != "NA": #if dead
            deathDate = datetime.strptime(x[7], '%Y-%m-%d')
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            timediff = todayDate - deathDate
            if timediff.days < 30:
                errors.append("ERROR: INDIVIDUAL: US36: Line: " + x[0] + " ID: " + x[1] + ": Death has occurred within the past 30 days.")
                problem = True
    if problem == True: 
        for i in errors: 
            print(str(i))
    return errors

def main(lists):
    recentDeaths(lists)

#type us36.main(allLists[2]) to test in readGed.py