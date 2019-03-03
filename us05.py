'''
User Story 05
Marriage before death

'''
from prettytable import PrettyTable
from datetime import datetime
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

def marriageBeforeDeath(input):
    names = []
    tags = []
    family = []
    
    result = []
    ans = []
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
                #set NAME_tag to first name 
                if names != []:
                    result.append(names)
                names = []
                names.append(NAME_tag)
                date_tag = "ALIVE"
                #set date_tag to ALIVE
            elif line[1] == "DEAT":
                date_tag = "DEAT"
                #set date_tag to DEAT
            elif line[1] == "FAMS":
                FAM_tag = line[2]
                #set FAM_tag to @F5@
                names.append(FAM_tag) 
            elif line[1] == "MARR":
                date_tag = "MARR"
                #set date_tag to MARR
        elif line[0] == str(2):
            if line[1] == "DATE":
                dates = (line[2]).split()
                if date_tag == "DEAT":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    #fixes format of dates into year-month-day
                    names.append("-".join(dates))
                elif date_tag == "MARR":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    #fixes format of dates into year-month-day
                    tags.append("-".join(dates))
    family.append(tags)
    result.append(names)
    #print(result)
    #print(family)

    error = False

    for i in family:
        if len(i) > 1:
            marr_date = datetime.strptime(i[1], '%Y-%m-%d')
            #print(marr_date)
            tag = i[0]
            #print(tag)
            for j in result:
                if tag in j:
                    if len(j) > 2:
                        #print("HE")
                        death_date = datetime.strptime(j[1], '%Y-%m-%d')
                        #print(death_date)
                        if(marr_date > death_date):
                            # print("ERROR: INDIVIDUAL: US05:" )
                            error = True
                            # print(ans)
                            ans.append(j)
    if error == True: 
        for i in ans: 
            return("ERROR: INDIVIDUAL: US05:" + str(i)) 
    return result

def main():
    try:
        inputGed = open("input_Rak05.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        print(marriageBeforeDeath(inputGed))

if __name__ == "__main__":
    main()