'''
User Story 32
List Multiple Births 

'''
import collections 
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

def checkMultipleBirths(inputGed):
    births = []
    result = []
    people = []
    family = []
    final_famList = []
    tags = []
    all_people = []
    all_fam = []
    if inputGed == "": 
        return []
    for i in inputGed: 
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI":  
                if people != []: 
                    all_people.append(people)
                    people = []
                people.append(line[1])
            elif line[2] == "FAM":
                if family != []:
                    all_fam.append(family)
                    family = [] 
                family.append(line[1])
        if line[1] == "TRLR": 
            all_fam.append(family)         
        elif line[1] == "BIRT": 
            tag = line[1]
        elif line[0] == str(2) and line[1] == "DATE":
            dates = (line[2]).split() 
            if tag == "BIRT": 
                formatDate(dates)
                people.append("/".join(dates))
                births.append("/".join(dates))
        elif line[1] == "HUSB": 
            family.append(line[2])
        elif line[1] == "WIFE": 
            family.append(line[2])
        elif line[1] == "CHIL": 
            family.append(line[2])
    date = [item for item, count in collections.Counter(births).items() if count > 1]
    for i in all_people: 
        if i[1] in date: 
            tags.append(i[0])
    for i in tags:
        for b in all_fam:
            if i in b: 
                final_famList.append(b[0])
    final = [item for item, count in collections.Counter(final_famList).items() if count > 1]
    if date == []: 
        return "No multiple births found"
    for i in date: 
        if len(date) == 1: 
            return "Family " + str(final[0]) + " experienced multiple birth dates on " + str(i)
        else: 
            result.append(i)
    return "Family "+ str(final) + " experienced multiple birth dates on " + str(result)
        

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
        print(checkMultipleBirths(inputGed2))


if __name__ == "__main__":
    main()