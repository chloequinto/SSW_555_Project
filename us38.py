'''
User Story 38
List upcoming birthdays
'''
from datetime import date, datetime

def upcomingBirthdays(input):
    notes = []
    for x in input: 
        if x[7] == "NA": #if alive
            try:
                birthDate = datetime.strptime(x[4], '%Y-%m-%d')
            except ValueError:
                birthDate = datetime.strptime("2019-04-01", '%Y-%m-%d')
            
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            timediff = birthDate - todayDate
            if timediff.days < 30:
                print("NOTE: INDIVIDUAL: US38: Line: " + x[0] + " ID: " + x[1] + ": Birthday occurring within the next 30 days.")
                notes.append("NOTE: INDIVIDUAL: US38: Line: " + x[0] + " ID: " + x[1] + ": Birthday occurring within the next 30 days.")
    
    return notes

def main(lists):
    upcomingBirthdays(lists)