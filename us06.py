'''
User Story 06
Divorce before death

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

def divorceBeforeDeath(input):
    names = []
    tags = []
    family = []
    res = []
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
                if names != []:
                    res.append(names)
                names = []
                names.append(NAME_tag)
                date_tag = "ALIVE"
            elif line[1] == "DEAT":
                date_tag = "DEAT"
            elif line[1] == "FAMS":
                FAM_tag = line[2]
                names.append(FAM_tag) 
            elif line[1] == "DIV":
                date_tag = "DIV"
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
                    names.append("-".join(dates))
                elif date_tag == "DIV":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    tags.append("-".join(dates))
    family.append(tags)
    res.append(names)
                        
    #print(res)
    #print(family)
    error = False
    for i in family:
        if len(i) > 1:
            div_date = datetime.strptime(i[1], '%Y-%m-%d')
            #print(div_date)
            tag = i[0]
            #print(tag)
            for j in res:
                if tag in j:
                    if len(j) > 2:
                        #print("HE")
                        death_date = datetime.strptime(j[1], '%Y-%m-%d')
                        #print(death_date)
                        if(death_date < div_date):
                            # print("ERROR: INDIVIDUAL: US06:" )
                            error = True
                            # print(ans)
                            ans.append(j)
    if error == True: 
        for i in ans: 
            print("ERROR: INDIVIDUAL: US06:" + str(i)) 
    #return ans      


def main():
    try:
        inputGed = open("input_6.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        print(divorceBeforeDeath(inputGed))

if __name__ == "__main__":
    main()
            