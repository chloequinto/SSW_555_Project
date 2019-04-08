'''
User Story 36
List recent deaths
'''
from datetime import date, datetime,timedelta

def recentDeaths(input):
    notes = []

    for x, y in zip(input[0], input[2]):
        if x[5] != "True": #if dead
            try:
                deathDate = datetime.strptime(x[6], '%Y-%m-%d')
            except ValueError:
                deathDate = datetime.strptime("2019-04-01", '%Y-%m-%d')
            
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            timediff = todayDate - deathDate
            if timediff.days < 30:
                print("NOTE: INDIVIDUAL: US36: Line: " + str(y[0]) + " ID: " + x[0] + ": Death has occurred within the past 30 days")
                notes.append("NOTE: INDIVIDUAL: US36: Line: " + str(y[0]) + " ID: " + x[0] + ": Death has occurred within the past 30 days")
        
    return notes

def main(lists):
    recentDeaths(lists)