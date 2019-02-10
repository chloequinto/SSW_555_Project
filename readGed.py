'''To Do 
1. Check that it works [x]
2. Try and Exception for inputs [x] 
3. sudo pip3 install Ptable [x]
4. Work on fam() function 
6. Unit Tests 
'''
from prettytable import PrettyTable 
from datetime import datetime

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


# This parser probably isn't needed, delete if you guys agree
def parser(inputGed): 
    global writeOutput
    for i in inputGed:
        writeOutput.write("--> " + i)
        inputSplit = i.strip().split(maxsplit=2)
        validLine = "N"
        if len(inputSplit) > 2 and inputSplit[2] in ["INDI", "FAM"]:
            if inputSplit[0] == "0":
                temp = inputSplit[2]
                inputSplit[2] = inputSplit[1]
                inputSplit[1] = temp
                validLine = "Y"
        elif inputSplit[0] in valid:
            if inputSplit[1] in valid[inputSplit[0]]:
                validLine = "Y"
        writeOutput.write("<-- " + inputSplit[0] + "|" + inputSplit[1] + "|" + validLine + "|" + " ".join(inputSplit[2:]) + "\n")
    print("All done!")


#Function to parse through and store families and individuals
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
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI" and new_individual == 1: 
                if alive == "False": 
                    indi_data.insert(5, "False") 
                    if is_child != "True": 
                        indi_data[7] = "Is not a child in this family"
                        if has_spouse != "True": 
                            indi_data[8] = "NO SPOUSE FOUND"
                    else: 
                        if has_spouse != "True": 
                            indi_data.append("NO SPOUSE FOUND")  
                elif alive != "False": 
                    indi_data.insert(5, "True")
                    indi_data.insert(6, "NA")
                    if is_child != "True": 
                        indi_data[7] = "Is not a child in this family"
                        if has_spouse != "True": 
                            indi_data.append("NO SPOUSE FOUND")
                    else: 
                        if has_spouse != "True": 
                            indi_data.append("NO SPOUSE FOUND") 
                indi_list.append(indi_data) 
                indi_data = []
                indi_data.append(line[1])
                has_spouse = "False"
                is_child = "False"
            elif line[2] == "FAM" and new_family == 1: 
                if is_married == "True": 
                    fam_data.insert(1, "Yes")
                    fam_data.insert(2, "No")
                    # fam_data[1] = "Yes"
                    # fam_data[2] = "No"
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
                indi_data.insert(5,"Is a child of couple: " + line[2])
            elif line[1] == "FAMS": 
                has_spouse = "True"
                indi_data.append(line[2])
                indi_data.insert(7, line[2])
            elif line[1] == "HUSB": 
                is_married = "True"
                fam_data.append(line[2])
            elif line[1] == "WIFE": 
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

    # for i in indi_list: 
    #     print(i)
    print(fam_list)
    #python can return things as a tuple so we can return both lists
    return (indi_list, fam_list)

           
                    
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
        y.add_row([j[0], j[1], j[2], j[3], j[3], j[4], j[0], j[0]])
    print(y) 

def main(): 
    global inputGed, writeOutput
    try:
        inputGed = open("input.ged", "r")
        writeOutput = open("output.txt", "w")
        
    except FileNotFoundError:
        print("Cannot open file")
    else:
        table(fam(inputGed))
    

if __name__ == "__main__": 
    main()
