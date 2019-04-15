'''
    User Story 39
    List upcoming anniversaries
    '''
from datetime import date, datetime

def upcomingAnniversaries(input, line):
    notes = []
    for x, b in zip(input, line):
        if x[2] == "NA": #if married
            try:
                anniDate = datetime.strptime(x[1], '%Y-%m-%d')
            except ValueError:
                anniDate = datetime.strptime("2019-04-01", '%Y-%m-%d')
            
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            timediff = anniDate - todayDate
            if timediff.days < 30:
                print("NOTE: FAMILY: US39: Line: " + str(b[0]) + " Husb ID: " + x[3] + " Husband Name: " + x[4] + " Wife ID: " + x[5] + " Wife Name: " + x[6] + ": Anniversary occurring within the next 30 days.")
                notes.append("NOTE: FAMILY: US39: Line: " + str(b[0]) + " Husb ID: " + x[3] + " Husband Name: " + x[4] + " Wife ID: " + x[5] + " Wife Name: " + x[6] + ": Anniversary occurring within the next 30 days.")
        else:
            pass

    return notes

def main(lists, line):
    upcomingAnniversaries(lists, line)
