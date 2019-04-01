'''
User Story 08
Birth before marriage of parents

'''

from datetime import date
from datetime import datetime,timedelta
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
            elif (tag == 'FAMC'):
                args = args.strip('@')
                individual[index].setChildIdentity(args)
            elif (tag == 'CHIL'):
                args = args.strip('@')
                family[index].setFamilyChildren(args)
            elif (tag == 'HUSB'):
                args = args.strip('@')
                family[index].setHusband(args)
            elif (tag == 'WIFE'):
                args = args.strip('@')
                family[index].setWife(args)
            elif (tag == 'MARR'):
                date = 'marriageDate'
            elif (tag == 'SEX'):
                individual[index].setSex(args)
        elif (level == '2') and (tag == 'DATE'):
            if(date == 'birthDate'):
                individual[index].setBirthDate(args)
            elif(date == 'marriageDate'):
                husband = family[index].getHusband()
                wife = family[index].getWife()
                individual[husband].setMarriageDate(args)
                individual[wife].setMarriageDate(args)
                family[index].setMarriageDate(args)
            elif(date == 'deathDate'):
                individual[index].setDeathDate(args)
            elif(date == 'divorceDate'):
                husband = family[index].getHusband()
                wife = family[index].getWife()
                individual[husband].setDivorceDate(args)
                individual[wife].setDivorceDate(args)
                family[index].setDivorceDate(args)
    return family


def formatDate(dates):
    date = dates.split()
    if (int(date[0]) in range(1, 10)):
        date[0] = "0" + date[0]
    month = months[date[1]]
    year = date[2]
    return (year + '-' + month + '-' + date[0])


class Individual(object):
    def __init__(self, ID='NA', birthDate='NA', marriageDate='NA',divorceDate='NA', childIdentity='NA', sex='NA'):
        self.ID = ID
        self.birthDate = birthDate
        self.marriageDate = marriageDate
        self.divorceDate = divorceDate
        self.childIdentity = childIdentity
        self.sex = sex

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

    def setChildIdentity(self, childIdentity):
        self.childIdentity = childIdentity

    def setSex(self, sex):
        self.sex = sex

    def getSex(self):
        return self.sex
  

class Family(object):
    def __init__(self, ID='NA', husband='NA', wife='NA', marriageDate='NA',divorceDate='NA'):
        self.ID = ID
        self.husband = husband
        self.wife = wife
        self.marriageDate = marriageDate
        self.divorceDate = divorceDate
        self.children = []

    def setHusband(self, husband):
        self.husband = husband

    def setWife(self, wife):
        self.wife = wife

    def getHusband(self):
        return self.husband

    def getWife(self):
        return self.wife

    def setMarriageDate(self, marriageDate):
        marriageDate = formatDate(marriageDate)
        self.marriageDate = marriageDate
    
    def setDivorceDate(self, divorceDate):
        divorceDate = formatDate(divorceDate)
        self.divorceDate = divorceDate

    def setFamilyChildren(self, children):
        self.children.append(children)

def checkDate(date1, date2):
    return date1 < date2


def BirthBeforeMarriageOfParents(fam,indi):
    if indi in individual:    
        if individual[indi].birthDate != 'NA' and family[fam].marriageDate != 'NA':
            firstCheck = checkDate(family[fam].marriageDate, individual[indi].birthDate)
            if family[fam].divorceDate != 'NA':
                divorceDate = datetime.strptime(family[fam].divorceDate, "%Y-%m-%d")
                birthDate = datetime.strptime(individual[indi].birthDate, "%Y-%m-%d")
                diffDate = birthDate - divorceDate
                secondCheck = True
                if diffDate.days > 273:
                    secondCheck = False
                result = firstCheck and secondCheck
                return result
            else:
                return firstCheck
                
        elif individual[indi].birthDate == 'NA':
            return True
        elif family[fam].marriageDate == 'NA':
            return True
        elif family[fam].divorceDate == 'NA':
            return True
    else:
        return True

def main(): 
    inputGed = open("Sprint2.ged", "r")
    family = parseGed(inputGed)
    return family
