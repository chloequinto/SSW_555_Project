'''
User Story 37
List recent survivors
'''
from datetime import date, datetime,timedelta

def indivDeaths(input, newFam):
    fams = []
    indivs = []
    #input = fam_list/ allLists[0]
    for i, b in zip(input, newFam):
        if i[0] != "NA": #each family
            fams = []
            fams.append(b[0]) #fam line number
            fams.append(i[0]) #fam tag
            fams.append(i[2]) #div date
            fams.append(i[3]) #husb id
            fams.append(i[5]) #wife id
            fams.append(i[6:][1:]) #children
            indivs.append(fams)

    return indivs

def checkFams(input, indivs):
    errors = []
    spouseid = []
    for i in input:
        for j in indivs:
            if i[6] != "NA": #if dead
                #j[3] == husb id and j[4] is wife id and j[5] is array of children
                if j[3] == i[0] or j[4] == i[0]: #checks if husb id or wife id == dead indiv
                    try:
                        deathDate = datetime.strptime(i[6], '%Y-%m-%d')
                    except ValueError:
                        deathDate = datetime.strptime("2019-04-01", '%Y-%m-%d')
                    if j[3] == i[0]:
                        spouseid = j[4]
                    if j[4] == i[0]:
                        spouseid = j[3]
                    today = date.today().strftime("%Y-%m-%d")
                    todayDate = datetime.strptime(today, "%Y-%m-%d")
                    timediff = (todayDate - deathDate)
                    #if divDate > deathDate:
                    if timediff.days < 30:
                        print("ERROR: FAMILY: US37: " + i[0] + ": passed within the last 30 days leaving behind their spouse: " + str(spouseid) + " and children: " + str(j[5]) + " on line " + str(j[0]))
                        errors.append("ERROR: FAMILY: US37: " + i[0] + ": passed within the last 30 days leaving behind their spouse: " + str(spouseid) + " and children: " + str(j[5]) + " on line " + str(j[0]))

    return errors


def main(inputindi, inputfam, newFam):
    #indivDeaths(tables[1])
    #allLists[0], allLists[1], allLists[3]
    return checkFams(inputindi, indivDeaths(inputfam, newFam))

