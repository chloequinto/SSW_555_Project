'''
User Story 10: 
Marriage after 14
'''

from datetime import datetime, timedelta

monthWordToInt = {
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

def marriageAfter14FamParse(input, newFam):
    fams = []
    indivs = []
    
    for i, b in zip(input, newFam): 
        if i[2] != "NA":
            fams = []
            fams.append(b[0])
            fams.append(i[0])
            fams.append(i[1])
            fams.append(i[3])
            fams.append(i[5])
            indivs.append(fams)
            
    # print(indivs)        
    return indivs

def checkIndividuals(indivs, familyparsed):
    errors = []
    for i in indivs:
        for j in familyparsed:
            if j[3] == i[0] or j[4] == i[0]: #check logic
                if i[3] != "NA": #if has a birthday 
                    try:
                        birthDate = datetime.strptime(i[3], '%Y-%m-%d')
                        marriageDate = datetime.strptime(j[2], '%Y-%m-%d') 
                    except ValueError:
                        birthDate = datetime.strptime("2018-01-01", '%Y-%m-%d') 
                        marriageDate = datetime.strptime("2018-01-01", '%Y-%m-%d') 
                    if(marriageDate < (birthDate+ timedelta(days=5475))):
                            print("ERROR: INDIVIDUAL: US10: " + i[0] + " marriage date occurs before they are 15 on line " + str(j[0]))
                            errors.append("ERROR: INDIVIDUAL: US10: " + i[0] + " marriage date occurs before they are 15 on line " + str(j[0]))

    return errors
                    

def main(individualTable, familyTable, newFam):
    return checkIndividuals(individualTable, marriageAfter14FamParse(familyTable, newFam))