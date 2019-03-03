'''
User Story 04
Marriage before divorce

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

def marriageBeforeDivorce(input):
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
            #if line[0] == 1
            if line[1] == "NAME":
                NAME_tag = line[2]
                #set NAME_tag to first name 
                if names != []:
                    result.append(names)
                names = []
                names.append(NAME_tag)
                date_tag = "ALIVE"
                #set date_tag to ALIVE
            elif line[1] == "MARR":
                date_tag = "MARR"
                #set date_tag to MARR
            elif line[1] == "DIV":
                date_tag = "DIV"
                #set date_tag to DIV
            elif line[1] == "FAMS":
                FAM_tag = line[2]
                #set FAM_tag to @F5@
                names.append(FAM_tag) 
        elif line[0] == str(2):
            #if line[0] == 2
            if line[1] == "DATE":
                dates = (line[2]).split()
                if date_tag == "MARR":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    #fixes format of dates into year-month-day
                    tags.append("-".join(dates))
                elif date_tag == "DIV":
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
        if len(i) > 2:
            marr_date = datetime.strptime(i[1], '%Y-%m-%d')
            #print(marr_date)
            tag = i[0]
            #print(tag)
            div_date = datetime.strptime(i[2], '%Y-%m-%d')

            if(marr_date > div_date):
                # print("ERROR: INDIVIDUAL: US04:" )
                error = True
                return("ERROR: INDIVIDUAL: US04:" + " The divorce date " + str(i[2]) + " is before the marriage date "  + str(i[1]))

            """ for j in result:
                if tag in j:
                    if len(j) > 2:
                        div_date = datetime.strptime(j[1], '%Y-%m-%d')
                        #print(div_date)
                        if(marr_date > div_date):
                            # print("ERROR: INDIVIDUAL: US04:" )
                            error = True
                            #return marr_date, div_date
                            # print(ans)
                            #ans.append(j) """


def main():
    try:
        inputGed = open("input_RakUS04.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        print(marriageBeforeDivorce(inputGed))

if __name__ == "__main__":
    main()