'''
User Story 32
List Multiple Births
'''
import collections


def checkMultipleBirths(lists):
    person = []
    bdays = []
    full_res = []
    res = []
    whole = []
    for i in lists: 
        bdays.append(i[4])
    date = [item for item, count in collections.Counter(bdays).items() if count > 1]
    for b in lists: 
        if b[4] in date: 
            
            person.append(b[1])
            person.append(b[0])
            whole.append(person)
            person = []
    for x, i in enumerate(whole): 
        print("ERROR: INDIVIDUAL: US32: " + str(i[0]) + " has the same birthdays as someone else on " + str(date) + " line " + str(i[1]))

        res.append("ERROR: INDIVIDUAL: US32: " + str(i[0]) + " has the same birthdays as someone else on " + str(date) + " line " + str(i[1])) 
    
    return res

def main(lists): 
    checkMultipleBirths(lists)
