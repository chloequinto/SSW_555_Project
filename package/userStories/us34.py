'''
User Story 34
List large age differences
'''

from datetime import datetime, timedelta

# Get lists of spouses
# Get their marriage date
# Subtract birthday from marriage date
# Compare ages*2 both ways
# Append to list

def largeAgeDifferences(inputIndi, inputFam, lineNum):
    indivs = []
    errors = []
    for i,b in zip(inputFam, lineNum):
        if i[1] != "NA":
            family = []
            family.append(i[0])
            family.append(i[1])
            family.append(i[3])
            family.append(i[5])
    
        for j in inputIndi:
            if j[0] == family[2]:
                husbandBirthday = j[3]
            if j[0] == family[3]:
                wifeBirthday = j[3]
        
        try:
            husbandBirthDate = datetime.strptime(husbandBirthday, '%Y-%m-%d')
            wifeBirthDate = datetime.strptime(wifeBirthday, '%Y-%m-%d')
            marriageDate = datetime.strptime(family[1], '%Y-%m-%d')
        except:
            husbandBirthDate = datetime.strptime("2018-01-01", '%Y-%m-%d')
            wifeBirthDate = datetime.strptime("2018-01-01", '%Y-%m-%d') 
            marriageDate = datetime.strptime("2018-01-01", '%Y-%m-%d')
        
        modWife = marriageDate - wifeBirthDate
        modHusband = marriageDate - husbandBirthDate

        if(modHusband >= (modWife*2)):
            fixString = "ERROR: INDIVIDUAL: US34: Individual " + family[2] + " was over twice as old as spouse " + family[3] + " at their time of marriage on line: "
            if fixString not in errors:
                print("ERROR: INDIVIDUAL: US34: Individual " + family[2] + " was over twice as old as spouse " + family[3] + " at their time of marriage on line: " + str(b[0]))
                errors.append(fixString)
        if(modWife >= (modHusband*2)):
            fixString2 = "ERROR: INDIVIDUAL: US34: Individual " + family[3] + " was over twice as old as spouse " + family[2] + " at their time of marriage on line: "
            if fixString2 not in errors:
                print("ERROR: INDIVIDUAL: US34: Individual " + family[3] + " was over twice as old as spouse " + family[2] + " at their time of marriage on line: " + str(b[0]))
                errors.append(fixString2)       
    return errors
                

def main(inputIndi, inputFam, lineNum):
    largeAgeDifferences(inputIndi, inputFam, lineNum)

