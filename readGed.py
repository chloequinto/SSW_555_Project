'''To Do 
1. Check that it works [x]
2. Try and Exception for inputs [x] 
3. sudo pip3 install Ptable [x]
4. Work on fam() function 
6. Unit Tests 
'''
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
    indi_list = []
    fam_list = []
    indi_data = []
    fam_data = []
    new_individual = 0
    new_family = 0
    has_spouse = "False"
    is_child = "False"
    for i in inputGed:
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
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
                # new_family = 0
            elif line[2] == "INDI" and new_individual == 0:
                indi_data.append(line[1])
                new_individual = 1
            elif line[2] == "FAM" and new_family == 0:
                fam_data.append(line[1])
                new_family = 1
            elif(line[1] in ['NOTE', 'HEAD', 'TRLR']):
                pass

        elif line[0] == str(1):
            if line[1] == "NAME":
                indi_data.append(line[2])
            elif line[1] == "SEX":
                indi_data.append(line[2])
            elif line[1] in ["BIRT", "DEAT"]:
                date_tag = line[1]
            elif line[1] == "FAMC":
                is_child = "True"
                indi_data.insert(5, "{'" + line[2] + "'}")
            elif line[1] == "FAMS":
                has_spouse = "True"
                indi_data.append("{'" + line[2] + "'}")
                indi_data.insert(7, "{'" + line[2] + "'}")
            elif line[1] == "HUSB":
                is_married = "True"
                fam_data = famHelper(fam_data, indi_list)
                fam_data.append(line[2])
            elif line[1] == "WIFE": 
                fam_data = famHelper(fam_data, indi_list)
                fam_data.append(line[2])
            elif line[1] == "CHIL":
                fam_data.append(line[2])

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
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    indi_data.insert(5, "-".join(dates))

    # indi_list.append(indi_data)
    # for i in indi_list:
    #     print(i)
    print(fam_list)
    # python can return things as a tuple so we can return both lists
    return (indi_list, fam_list)

#tried to add names of husband and wife
def famHelper(famList, indiList):
    if len(famList) > 4 and famList[3] == indiList[0]:
        if indiList[2] == "F":
            famList.insert(6, indiList[1])
        else:
            famList.insert(4, indiList[1])

    return famList
                    
#Function to write the table 
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
    print("Families")

    for j in lists[1]:
        y.add_row([j[0], j[1], j[2], j[3], j[3], j[4], j[0], j[5:]])
    print(y)


def main():
    global inputGed
    try:
        inputGed = open("input.ged", "r")
        # writeOutput = open("output.txt", "w")

    except FileNotFoundError:
        print("Cannot open file")
    else:
        table(fam(inputGed))


if __name__ == "__main__":
    main()
