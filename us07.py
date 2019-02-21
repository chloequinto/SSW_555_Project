#User Story 7 

import re
from datetime import datetime

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

def storeData(inputGed): 
    res = []
    full = []
    if inputGed == "": 
        return []
    for i in inputGed: 
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        if line[0] == str(0) and line[1] == "TRLR": 
            full.append(res)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI": 
                if res != []: 
                    full.append(res)
                res = []
                res.append(line[1])
        elif line[1] in ["BIRT", "DEAT"]:
            date_tag = line[1]
        elif line[0] == str(2) and line[1] == "DATE":
            dates = (line[2]).split() 
            if date_tag == "BIRT": 
                formatDate(dates)
                res.append(line[2])
            elif date_tag == "DEAT": 
                formatDate(dates)
                res.append(line[2])
    return full 

def checkForLessThan150(data): 
    '''
    Function that checks: 
    1.  Death should be less than 150 years
    the birth of dead people
    2.  Current date should be less 
    than 150 years after the birth for all living people 
    '''
    for i in data: 
        print(i)
        if (len(i) <= 2): #still alive 
            # print("still alive")
            birthDate = i[1]
            print(birthDate)
            # deathDate = datetime.strptime(i[2], '%Y-%m-%d')
        if (len(i) > 2):
            print("DEAD")
            birthDate = datetime.strptime(i[1], '%d %b %Y')
            deathDate = datetime.strptime(i[2], '%d %b %Y')
def formatDate(dates): 
    dates[1] = monthWordToInt[dates[1]]
    if (int(dates[0]) < 10):
        dates[0] = "0" + dates[0]
    temp = dates[1]
    dates[1] = dates[0]
    dates[0] = temp

def main(): 
    try: 
        inputGed = open("input.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        
    except FileNotFoundError:
        print("Can't open the file")
    else:
        checkForLessThan150(storeData(inputGed))


if __name__ == "__main__":
    main()