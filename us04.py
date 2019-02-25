'''
Rakshak Kumar

User Story 04
Marriage before divorce

'''

from prettytable import PrettyTable
from datetime import datetime

import re

monthNumbers = {
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

def marriageBeforeDivorce(input):
    names = []
    tags = []
    family = []
    
    result = []
    reply = []
    date_tag = "Null"
    
    for i in input:
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "FAM":
                FAM_tag = line[1]
                if tags != []:
                    family.append(tags)
                tags = []
                tags.append(FAM_tag)
        
        elif line[0] == str(1):
            if line[1] == "NAME":
                NAME_tag = line[2] 
                if names != []:
                    result.append(names)
                names = []
                names.append(NAME_tag)
                date_tag = "ALIVE"
            elif line[1] == "DIV":
                date_tag = "DIV"
            elif line[1] == "FAMS":
                FAM_tag = line[2]
                names.append(FAM_tag) 
            elif line[1] == "MARR":
                date_tag = "MARR"
        
        elif line[0] == str(2):
            if line[1] == "DATE":
                dates = (line[2]).split()
                if date_tag == "DIV":
                    dates[1] = monthNumbers[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    names.append("-".join(dates))
                
                elif date_tag == "MARR":
                    dates[1] = monthNumbers[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    tags.append("-".join(dates))
    family.append(tags)
    result.append(names)
                        
    print(result)
    print(family)

    for i in family:
        if len(i) > 1:
            marr_date = datetime.strptime(i[1], '%Y-%m-%d')
            tag = i[0]
            for j in result:
                if tag in j:
                    if len(j) > 2:
                        divorce_date = datetime.strptime(j[1], '%Y-%m-%d')
                        if(divorce_date < marr_date):
                            print("Error! Marriage has to be before Divorce!")
                            reply.append(j)
    print(reply)        

def main():
    try:
        inputGed = open("input_2.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        marriageBeforeDivorce(inputGed)

if __name__ == "__main__":
    main()
            
