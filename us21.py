'''
User Story 21
Correct gender for role

'''


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
            if (tag == 'HUSB'):
                args = args.strip('@')
                family[index].setHusband(args)
            elif (tag == 'WIFE'):
                args = args.strip('@')
                family[index].setWife(args)
            elif (tag == 'MARR'):
                date = 'marriageDate'
            elif (tag == 'SEX'):
                individual[index].setSex(args)
        
    return family


class Individual(object):
    def __init__(self, ID='NA', birthDate='NA', marriageDate='NA', deathDate='NA', divorceDate='NA', sex='NA'):
        self.ID = ID
        self.birthDate = birthDate
        self.marriageDate = marriageDate
        self.deathDate = deathDate
        self.divorceDate = divorceDate
        self.sex = sex

    
    def setSex(self, sex):
        self.sex = sex

    def getSex(self):
        return self.sex


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


def CheckGenderForRole(index):
    husband = family[index].getHusband()
    wife = family[index].getWife()
    if(individual[husband].getSex() != 'M'):
        return False
    if(individual[wife].getSex() != 'F'):
        return False
    else:
        return True




def main():
    inputGed = open("Sprint1.ged", "r")
    family = parseGed(inputGed)
    return family
