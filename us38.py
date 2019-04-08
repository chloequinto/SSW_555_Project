'''
User Story 38
List upcoming birthdays
'''
from datetime import date, datetime

def upcomingBirthdays(input, line):
    notes = []
    for x, b in zip(input, line): 
        if x[5] == "True": #if alive
            try:
                birthDate = datetime.strptime(x[5], '%Y-%m-%d')
            except ValueError:
                birthDate = datetime.strptime("2019-04-01", '%Y-%m-%d')
            
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            timediff = birthDate - todayDate
            if timediff.days < 30:
                print("NOTE: INDIVIDUAL: US38: Line: " + str(b[0]) + " ID: " + x[1] + ": Birthday occurring within the next 30 days.")
                notes.append("NOTE: INDIVIDUAL: US38: Line: " + str(b[0]) + " ID: " + x[1] + ": Birthday occurring within the next 30 days.")
        else: 
            pass
    
    return notes

def main(lists, line):
    upcomingBirthdays(lists, line)