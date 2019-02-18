from prettytable import PrettyTable
from datetime import datetime
import re
valid = {
    "0": ("HEAD", "TRLR", "NOTE"),
    "1": ("NAME", "SEX", "BIRT", "DEAT", "DIV", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL"),
    "2": ("DATE")
}

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


# Function to parse through and store families and individuals
def fam(inputGed):
    names = {}
    indi_list = []
    fam_list = []
    indi_data = []
    fam_data = []
    new_individual = 0
    new_family = 0
    has_spouse = "False"
    is_child = "False"
    birth_year = 0
    for i in inputGed:
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        if line[0] == str(0) and line[1] == "TRLR": 
            if is_married == "True":
                fam_data.insert(1, "Yes")
                fam_data.insert(2, "NA")
            else: #if divorced
                fam_data[1] = "No"
                fam_data[1] = "Yes"
            fam_list.append(fam_data)
            fam_data = []
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI" and new_individual == 1:
                if alive == "False":
                    indi_data.insert(5, "False")
                    if is_child != "True":
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data[8] = "NA"
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")
                elif alive != "False":
                    indi_data.insert(5, "True")
                    indi_data.insert(6, "NA")
                    if is_child != "True":
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data.append("NA")
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")

                indi_list.append(indi_data)
                indi_data = []
                ID_tag = line[1]
                indi_data.append(line[1])

                has_spouse = "False"
                is_child = "False"
            elif line[2] == "FAM" and new_family == 1:
                if is_married == "True":
                    fam_data.insert(1, "Yes")
                    fam_data.insert(2, "NA")
                else: #if divorced
                    fam_data[1] = "No"
                    fam_data[1] = "Yes"
                fam_list.append(fam_data)
                fam_data = []
                fam_data.append(line[1])
            elif line[2] == "INDI" and new_individual == 0:
                ID_tag = line[1]
                indi_data.append(line[1])
                new_individual = 1
            elif line[2] == "FAM" and new_family == 0:
                if alive == "False":
                    indi_data.insert(5, "False")
                    if is_child != "True":
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data[8] = "NA"
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")
                elif alive != "False":
                    indi_data.insert(5, "True")
                    indi_data.insert(6, "NA")
                    if is_child != "True":
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data.append("NA")
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")
                indi_list.append(indi_data)
                fam_data.append(line[1])
                new_family = 1
            elif(line[1] in ['NOTE', 'HEAD']):
                pass

        elif line[0] == str(1):
            if line[1] == "NAME":
                NAME_tag = line[2]
                names[ID_tag] = NAME_tag
                indi_data.append(line[2])
            elif line[1] == "SEX":
                indi_data.append(line[2])
            elif line[1] in ["BIRT", "DEAT"]:
                date_tag = line[1]
            elif line[1] == "FAMC":
                is_child = "True"
                indi_data.insert(6, "{'" + line[2] + "'}")
            elif line[1] == "FAMS":
                has_spouse = "True"
                indi_data.append("{'" + line[2] + "'}")
                indi_data.insert(7, "{'" + line[2] + "'}")
            elif line[1] == "HUSB":
                is_married = "True"
                # fam_data = famHelper(fam_data, indi_list)
                fam_data.append(line[2])
            elif line[1] == "WIFE": 
                # fam_data = famHelper(fam_data, indi_list)
                fam_data.append(line[2])
            elif line[1] == "CHIL":
                fam_data.append("'" + line[2] + "'")

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
                    indi_data.append("-".join(dates))
                    birthDateMed = ("-".join(dates))
                    birthDate = datetime.strptime(birthDateMed, '%Y-%m-%d')
                    current = datetime.now()
                    birth_year = int(dates[0])
                    indi_data.append(current.year - birth_year)
                    alive = "True"
                elif date_tag == "DEAT":
                    alive = "False"
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    death_year = int(dates[2])
                    indi_data[4] = death_year - birth_year
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    indi_data.insert(5, "-".join(dates))
                    deathDateMed = ("-".join(dates))
                    deathDate = datetime.strptime(deathDateMed, '%Y-%m-%d')
    for i in indi_list:
        if alive == "True":
            print("Individual: " + indi_data[1] + " is still alive")
        elif(deathDate > birthDate):
            print("Pass: " + indi_data[1])
        else:
            print("Individual: " + indi_data[1] + " has a birth date after their death date")

    #change names 
    for i in fam_list: 
        if i[3] in names: 
            i.insert(4, names[i[3]])
        if i[5] in names: 
            i.insert(6, names[i[5]])
    return (indi_list, fam_list)


#Function to write the table 
def table(lists): 
    global names 
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
                     'Alive', 'Death', 'Child', 'Spouse']

    for i in lists[0]:
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
    print("\nIndividuals")
    print(x)


    y = PrettyTable()
    y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID',
                     'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    print("\nFamilies")

    for j in lists[1]:
        children = ""
        if (len(j[6:]) > 0):
            children = "{" + ", ".join(j[7:]) + "}"
        else:
            children = 'NA'
        y.add_row([j[0], j[1], j[2], j[3], j[4], j[5], j[6], children])
    print(y)

# def helper(): 

def main():
    global inputGed
    try:
        inputGed = open("input_1.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        table(fam(inputGed))


if __name__ == "__main__":
    main()



'''
User Story 03
Birth before death
'''
'''
import datetime

def birthBeforeDeath(inputGed):
    births = []
    deaths = []
    people = {}
    if inputGed == "":
        return []
    for i in inputGed:
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI": 
                name = line[1]
        elif line[1] == "NAME":
            name = line[2]
        elif line[1] == "BIRT": 
            tag = line[1]
        elif line[1] == "DEAT":
            tag = line[1]
        elif line[0] == str(2) and line[1] == "DATE": 
            if tag == "BIRT": 
                people.append(line[2])
                births.append(line[2])
            elif tag == "DEAT": 
                people.append(line[2])
                deaths.append(line[2])
    print("\n")
    print(people)
    print("\n")
    print(deaths)
    print("\n")
    print(births)

def main(): 
    try: 
        inputGed = open("input.ged", "r")
        
    except FileNotFoundError:
        print("Can't open the file")
    else:
       birthBeforeDeath(inputGed)


if __name__ == "__main__":
    main()
'''
'''
def birthBeforeDeath(lists):
    for i in lists[2]:
        birthDate = datetime.strptime(lists[i], '%Y-%m-%d')
        deathDate = datetime.strptime(lists[3][i], '%Y-%m-%d')
        if(deathDate > birthDate):
            print("Wow")
            return True
        
        else:
            print("Error: Individual: has their date of death before their date of birth")
            return False

'''