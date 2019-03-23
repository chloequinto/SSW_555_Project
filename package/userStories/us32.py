'''
User Story 32
'''
import collections


def checkMultipleBirths(lists):
    person = []
    bdays = []
    res = []
    for i in lists: 
        bdays.append(i[3])
    date = [item for item, count in collections.Counter(bdays).items() if count > 1]
    for b in lists: 
        if b[3] in date: 
            person.append(b[0])
    for i in person: 
        print("ERROR: INDIVIDUAL: US32: " + str(i) + " has the same birthdays as someone else on " + str(date))
        res.append("ERROR: INDIVIDUAL: US32: " + str(i) + " has the same birthdays as someone else on " + str(date))
    return res

def main(lists): 
    checkMultipleBirths(lists)
