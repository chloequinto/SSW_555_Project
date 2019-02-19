'''
User Story 03
Birth before death

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



def birthBeforeDeath(input):
    names = []
    birth = []
    death = []
    res = []
    ans = []
    new_indi = 0
    has_death = 0

    for i in input:
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        
        if line[0] == str(1):
            if line[1] == "NAME":
                NAME_tag = line[2] #hello! names, yeah the full name. ok should that be a little further down?
                if names != []:
                    res.append(names)
                names = []
                names.append(NAME_tag)#what is the list that you store everyting in OOOOOO I see yeah
         
                new_indi = 1
            elif line[1] == "BIRT":
                date_tag = "BIRT"
                has_death = 0
            elif line[1] == "DEAT":
                date_tag = "DEAT"
                has_death = 1
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
                elif date_tag == "DEAT":
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    names.append("-".join(dates))

    for i in res:
        if (len(i)!=3):
            print(i[0] + " is still alive")
        else:
            birthDate = datetime.strptime(i[1], '%Y-%m-%d')
            deathDate = datetime.strptime(i[2], '%Y-%m-%d')

            if birthDate > deathDate:
                print("Error: " + i[0] + "has a birth date after their death date")
                ans.append(i)
            else:
                print(i[0] + " has passed")
                
    print(ans)
    return(ans)

    
                    

def main():
    try:
        inputGed = open("input.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        birthBeforeDeath(inputGed)

if __name__ == "__main__":
    main()