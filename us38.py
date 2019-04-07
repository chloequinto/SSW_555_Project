'''
User Story 38
List upcoming birthdays
'''
from prettytable import PrettyTable
import re
from datetime import date
from datetime import datetime,timedelta
import readGed

def upcomingBirthdays(input):
    problem = False
    errors = []
    for x in input: 
        if x[7] == "NA": #if alive
            birthDate = datetime.strptime(x[4], '%Y-%m-%d')
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            timediff = birthDate - todayDate
            if timediff.days < 30:
                errors.append("ERROR: INDIVIDUAL: US38: Line: " + x[0] + " ID: " + x[1] + ": Birthday occurring within the next 30 days.")
                problem = True
    if problem == True: 
        for i in errors: 
            print(str(i))
    return errors

def main(lists):
    upcomingBirthdays(lists)

#type us38.main(allLists[2]) to test in readGed.py