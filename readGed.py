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
    for i in inputGed: 
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[2] == "INDI":
            Individual_Table["ID"].append(line[1])
        elif line[0] == "1" and line[1] == "NAME": 
            Individual_Table["NAME"].append(line[2])
        elif line[0] == "1" and line[1] == "SEX":
            Individual_Table["SEX"].append(line[2])
        # elif line[0] == "1" and line[1] == "BIRT" :
        #     # add date somehow 
        #     if line[1] == "DEAT":
        #         #read death day to 
        #         Individual_Table["ALIVE"].append("") #date added
        #     else:
        #         Individual_Table["ALIVE"].append("NA")
        elif line[0] == "1" and line[1] == "DEAT": # you reach a problem here
            if line[2] == "Y": 
                Individual_Table["ALIVE"].append("False")
            else:
                Individual_Table["ALIVE"].append("TRUE")
        elif line[0] == "1" and (line[1] == "HUSB" or line[1] == "WIFE"):
            Individual_Table["SPOUSE"].append(line[2])
        elif line[0] == "1" and (line[1] == "CHIL"): #you reach a problem here
            #not every individual has a child
            #need another parameter to check for individuals
            #propose a different data structure and possibly have pointers 
            Individual_Table["CHIL"].append(line[2])

    print(Individual_Table)

def split_them_lines(lines): 
    '''Function to split the given line into the corresponding elements ''' 
    #necessary for getting that death year compare to datetime
    b = line.split(' ', 2)
    level = b[0]
    tag = b[1].strip()
    if (b[2] != ''): 
        arg = b[2].strip()
    else: 
        arg = ''
    return [level, tag, arg]
    

#Function to write the table 
def table(): 
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 
                    'Alive', 'Death', 'Child', 'Spouse']

    for i in Individual_Table.items(): 
        x.add_row([i.ID, i.NAME, i.GENDER, i.BIRTHDAY, i.AGE, 
        i.ALIVE, i.DEATH, i.CHILD, i.SPOUSE ])
    print("\nIndividuals")
    print(x)
    
    y = PrettyTable()
    y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID',
                    'Husband Name', 'Wife ID', 'Wife Name', 'Children']
    print("Families")  

    for j in Family_Table.items():
        y.add_row([j.ID, j.MARRIED, i.DIVORCED, i.HUSBANDid, 
        i.HUSBANDname, i.WIFEid, i.WIFEname, i.CHILDREN])
    print(y) 

def main(): 
    global inputGed, writeOutput
    try:
        inputGed = open("input.ged", "r")
        print("Opening files")
        writeOutput = open("output.txt", "w")
        
    except FileNotFoundError:
        print("Cannot open file")
    else:
        fam(inputGed)
        # table()
    

if __name__ == "__main__": 
    main()
