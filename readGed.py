

from prettytable import PrettyTable
from datetime import datetime
import re
import us29, us16
import us01, us02
import us03, us06
from package.userStories import us07, us32

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
    #change names 
    for i in fam_list: 
        if i[3] in names: 
            i.insert(4, names[i[3]])
        if i[5] in names: 
            i.insert(6, names[i[5]])
    return (indi_list, fam_list)


# Function to write the table
# move to individual files maybe
def table(lists): 
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
        children = "NA"
        if (len(j[6:]) > 0):
            children = "{" + ", ".join(j[7:]) + "}"
        y.add_row([j[0], j[1], j[2], j[3], j[4], j[5], j[6], children])
    print(y)

def main():
    try:
        inputGed = open("inputRZ2.ged", "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        allLists = fam(inputGed)
        table(allLists)
        
        if us07.checkForLessThan150(inputGed) != True: 
            print("\nERROR: INDIVIDUAL: US07: Current Age > 150 or Death - Birth  > 150")
        value = us32.checkMultipleBirths(inputGed)
        if value != []: 
            print('ERROR: FAMILY: US32: ' + value )
        individual = us01.main()
        for indi in individual:
            us01Test_Birth = us01.BirthBeforeCurrent(indi)
            if us01Test_Birth !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Birthday " + individual[indi].birthDate + " occurs in the future")
            us01Test_Death = us01.DeathBeforeCurrent(indi)
            if us01Test_Death !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Death date " + individual[indi].deathDate + " occurs in the future")
            us01Test_Marriage = us01.MarriageBeforeCurrent(indi)
            if us01Test_Marriage !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Marriage date " + individual[indi].marriageDate + " occurs in the future")
            us01Test_Divorce = us01.DivorceBeforeCurrent(indi)
            if us01Test_Divorce !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Divorce date " + individual[indi].divorceDate + " occurs in the future")
            us02Test = us02.BirthBeforeMarriage(individual[indi])
            if us02Test != True:
                print("ERROR: INDIVIDUAL: US02: "+ individual[indi].ID + ": Birthday " + individual[indi].birthDate + " occurs before marriage " + individual[indi].marriageDate)
        
        us03.main()
        us06.main()  
        us16.main(allLists[0])
        us29.deaths(allLists[0]) 
        print("\n")
if __name__ == "__main__":
    main()
