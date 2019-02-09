'''To Do 
1. Check that it works 
2. Try and Exception for inputs [x] 
3. sudo pip3 install Ptable
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

Individual_Table = {
    'ID': [],
    'NAME': [],
    'SEX': [],
    'BIRT': [],
    'AGE': [], 
    'ALIVE': [],
    'DEAT': [],
    'CHIL': [],
    'SPOUSE': []
}

Family_Table = {
    'ID': [],
    'MARR': [],
    'DIV': [],
    'HUSID': [],
    'HUSNAME': [],
    'WIFEID': [],
    'WIFENAME': [],
    'CHIL': []
}


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
    new_individual = 0 #used to check if new individual 
    # if new_individual = 0 -> true 
    # if new_individual = 1 -> false -> append old values 
    new_family = 0 #used to check if new family 
    for i in inputGed:
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI" and new_individual == 1: #if this is an instance that we see a new person
                indi_list.append(indi_data) 
                indi_data = []
                indi_data.append(line[1])
            # elif new_family == 1: #if this is an instance that we see a new family 
            #     fam_list.append(fam_data)
            #     fam_data = []
            #     new_family = 0 
            elif line[2] == "INDI" and new_individual == 0: 
                indi_data.append(line[1])
                new_individual = 1 
            # elif line[2] == "FAM" and new_individual == 0: 
            #     new_family = 1
            #     fam_data.append(line[1])
           
           
        elif line[0] == str(1): 
            if line[1] == "NAME": 
                indi_data.append(line[2])
            elif line[1] == "SEX": 
                indi_data.append(line[2])
            elif line[1] == "BIRT":
                indi_data.append("12 27 1997")
                indi_data.append("21")
                indi_data.append("Y")
                
                indi_data.append("N")
                indi_data.append("the child")
            elif line[1] == "FAMS": 
                indi_data.append(line[2])
            elif line[1] == "FAMC": 
                indi_data.append(line[2])
        else: 
           pass
    print(indi_list)
    return indi_list

           
                    
#Function to write the table 
def table(indi_list): 
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 
                    'Alive', 'Death', 'Child', 'Spouse']

    for i in indi_list: 
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        # print(i[0])
    print("\nIndividuals")
    print(x)
    
    y = PrettyTable()
    y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID',
                    'Husband Name', 'Wife ID', 'Wife Name', 'Children']
    print("Families")  

    # for j in Family_Table.items():
    #     y.add_row([j.ID, j.MARRIED, i.DIVORCED, i.HUSBANDid, 
    #     i.HUSBANDname, i.WIFEid, i.WIFEname, i.CHILDREN])
    print(y) 

def main(): 
    global inputGed, writeOutput
    try:
        inputGed = open("input.ged", "r")
        # print("Opening files")
        writeOutput = open("output.txt", "w")
        
    except FileNotFoundError:
        print("Cannot open file")
    else:
        # fam(inputGed)
        table(fam(inputGed))
    

if __name__ == "__main__": 
    main()
