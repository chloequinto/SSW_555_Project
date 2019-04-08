'''
User Story 02
Birth before marriage

'''

from datetime import date
from datetime import datetime
from collections import OrderedDict


individual = OrderedDict()
family = OrderedDict()
months = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12",
}


def parseGed(inputGed):
    for line in inputGed:
        values = line.split()
        level = values[0]
        tag = values[1]
        args = ' '.join(values[2:])
        if(tag[0] == '@'):
            tag = values[2]
            args = values[1]

        if(level == '0'):
            args = args.strip('@')
            index = args
            if(tag == 'INDI'):
                individual[index] = Individual(args)
            elif (tag == 'FAM'):
                family[index] = Family(args)
        elif (level == '1'):
            if(tag == 'BIRT'):
                date = 'birthDate'
            elif (tag == 'DEAT'):
                date = 'deathDate'
            elif (tag == 'DIV'):
                date = 'divorceDate'
            elif (tag == 'HUSB'):
                args = args.strip('@')
                family[index].setHusband(args)
            elif (tag == 'WIFE'):
                args = args.strip('@')
                family[index].setWife(args)
            elif (tag == 'MARR'):
                date = 'marriageDate'
        elif (level == '2') and (tag == 'DATE'):
            if(date == 'birthDate'):
                individual[index].setBirthDate(args)
            elif(date == 'marriageDate'):
                husband = family[index].getHusband()
                wife = family[index].getWife()
                individual[husband].setMarriageDate(args)
                individual[wife].setMarriageDate(args)
            elif(date == 'deathDate'):
                individual[index].setDeathDate(args)
            elif(date == 'divorceDate'):
                husband = family[index].getHusband()
                wife = family[index].getWife()
                individual[husband].setDivorceDate(args)
                individual[wife].setDivorceDate(args)
    return individual


def formatDate(dates):
    date = dates.split()
    if (int(date[0]) in range(1, 10)):
        date[0] = "0" + date[0]
    month = months[date[1]]
    year = date[2]
    return (year + '-' + month + '-' + date[0])


class Individual(object):
    def __init__(self, ID='NA', birthDate='NA', marriageDate='NA'):
        self.ID = ID
        self.birthDate = birthDate
        self.marriageDate = marriageDate

    def setBirthDate(self, birthDate):
        birthDate = formatDate(birthDate)
        self.birthDate = birthDate

    def setMarriageDate(self, marriageDate):
        marriageDate = formatDate(marriageDate)
        self.marriageDate = marriageDate

    def setDeathDate(self, deathDate):
        deathDate = formatDate(deathDate)
        self.deathDate = deathDate

    def setDivorceDate(self, divorceDate):
        divorceDate = formatDate(divorceDate)
        self.divorceDate = divorceDate


  

class Family(object):
    def __init__(self, ID='NA', husband='NA', wife='NA', marriageDate='NA'):
        self.ID = ID
        self.husband = husband
        self.wife = wife
        self.marriageDate = marriageDate

    def setHusband(self, husband):
        self.husband = husband

    def setWife(self, wife):
        self.wife = wife

    def getHusband(self):
        return self.husband

    def getWife(self):
        return self.wife


def checkDate(date1, date2):
    dateTime1 = datetime.strptime(str(date1), "%Y-%m-%d")
    dateTime2 = datetime.strptime(str(date2), "%Y-%m-%d")
    return dateTime1.date() < dateTime2.date()


def BirthBeforeMarriage(individual):
    if individual.birthDate != 'NA' and individual.marriageDate != 'NA':
        return checkDate(individual.birthDate, individual.marriageDate)
    elif individual.birthDate == 'NA':
        return True
    elif individual.marriageDate == 'NA':
        return True


def main(): 
    inputGed = open("Sprint2.ged", "r")
    individual = parseGed(inputGed)
    return individual