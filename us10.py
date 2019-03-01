'''
User Story 10: 
Marriage after 14
'''

from prettytable import PrettyTable
from datetime import datetime
from datetime import timedelta
import re

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

def marriageAfter14(inputs):
    names = []
    tags = []
    family = []
    res = []
    errors = []
    date_tag = "Null"


    for i in inputs:
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "FAM":
                FAM_tag = line[1]
                if tags != []:
                    family.append(tags)
                tags = []
                tags.append(FAM_tag)
            elif line[2] == "INDI":
                NAME_tag = line[1] 
                if names != []:
                    res.append(names)
                names = []
                names.append(NAME_tag)
                date_tag = "None"

        elif line[0] == str(1):    
            if line[1] == "BIRT":
                date_tag = "BIRT"
            elif line[1] == "FAMS":
                FAM_tag = line[2]
                names.append(FAM_tag) 
            elif line[1] == "MARR":
                date_tag = "MARR"
        elif line[0] == str(2):
            if line[1] == "DATE":
                dates = (line[2]).split()
                if date_tag == "BIRT":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    names.append("-".join(dates))
                elif date_tag == "MARR":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    tags.append("-".join(dates))
    family.append(tags)
    res.append(names)

    error = False
    for i in family:
        if len(i) > 1:
            marr_date = datetime.strptime(i[1], '%Y-%m-%d')
            famTag = i[0]
            for j in res:
                if famTag in j:
                    if len(j) > 2:
                        birth_date = datetime.strptime(j[1], '%Y-%m-%d')
                        #print(marr_date - (birth_date + timedelta(days=5475)))
                        if(marr_date < (birth_date+ timedelta(days=5475))):
                            print("ERROR: INDIVIDUAL: US10: " + j[0] + " marriage date occurs before they are 15\n")
                            errors.append("ERROR: INDIVIDUAL: US10: " + j[0] + " marriage date occurs before they are 15")
                            error = True
    return errors
                    

def main():
    try:
        inputGed = open("Matt_input3.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        marriageAfter14(inputGed)

if __name__ == "__main__":
    main()
