"""
User Story 42: 
Reject invalid dates
"""

import re

marriageDates = {}
birthDates = {}
deathDates = {}
divorceDates = {}

daysW31 = [1, 3, 5, 7, 8, 10, 12]
daysW30 = [4, 6, 9, 11]

def filterDates(inputs):
    indi = inputs[0]
    families = inputs[1]

    for i in indi:
        if i[3] != "NA":
            if i[0] not in birthDates:
                birthDates[i[0]] = ""
            
            birthDates[i[0]] = i[3]
        if i[6] != "NA":
            if i[0] not in deathDates:
                deathDates[i[0]] = ""
            deathDates[i[0]] = i[6]
    
    for i in families:
        if i[1] != "NA":
            if i[0] not in marriageDates:
                marriageDates[i[0]] = ""
            marriageDates[i[0]] = i[1]
        if i[2] != "NA":
            if i[0] not in divorceDates:
                divorceDates[i[0]] = ""
            divorceDates[i[0]] = i[2]
    # print(birthDates)
    badBirth = rejectBadDates(birthDates, "birthday")
    badMarriage = rejectBadDates(marriageDates, "marriage")
    badDeath = rejectBadDates(deathDates, "death")
    badDivorce = rejectBadDates(divorceDates, "divorce")

    return not badBirth and not badMarriage and not badDeath and not badDivorce

def rejectBadDates(dateDict, column):
    hasBadDates = False

    indiOrFam = "INDIVIDUAL" if (column == "birthday" or column == "death") else "FAMILY"
    
    for specificId, date in dateDict.items():
        # print(date)
        regex = re.compile(r"^([0-9]{4}-[0-9]{2}-[0-9]{2})$")
        if len(date) != 10:
            print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correct number of digits for their {column}.")
            hasBadDates = True
        elif not regex.match(date):
            print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correctly formatted date for their {column}.")
            hasBadDates = True
        # if month is greater than 12
        elif int(date[5:7]) > 12:
            print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correct month for their {column}.")
            hasBadDates = True
        # correct number of days in months
        
        elif int(date[5:7]) in daysW31:
            # print(date[5:7]+" "+date[8:])
            if int(date[8:]) > 31:
               
                print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correct day for their {column}.")
                hasBadDates = True
        elif int(date[5:7]) in daysW30:
            if int(date[8:]) > 30:
                print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correct day for their {column}.")
                hasBadDates = True
        elif date[5:7] == "02":
            if int(date[8:]) > 29:
                print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correct day for their {column}.")
                hasBadDates = True
            elif date[8:] == "29" and int(date[0:3]) % 4 != 0:
                print(f"ERROR: {indiOrFam}: US42: {specificId} does not have the correct day for their {column}.")
                hasBadDates = True
    
    return hasBadDates