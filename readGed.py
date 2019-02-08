'''To Do 
1. Check that it works 
2. Try and Exception for inputs [x] 
3. sudo pip3 install Ptable
4. Work on fam() function 
6. Unit Tests 
'''
from prettytable import PrettyTable 
valid = {
    "0": ("HEAD", "TRLR", "NOTE"),
    "1": ("NAME", "SEX", "BIRT", "DEAT", "DIV", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL"),
    "2": ("DATE")
}

# Individual_Table = {}
# Family_Table = {}

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
# def fam(): 
    #TO DO 
    #Parse through the ged file for IDs
    # append to Individual_Table or Family_Table


#Function to write the table 
def table(): 
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 
                    'Alive', 'Death', 'Child', 'Spouse']
    #UNCOMMENT 
    # for i in Individual_Table.items(): 
    #     x.add_row([i.ID, i.NAME, i.GENDER, i.BIRTHDAY, i.AGE, 
    #     i.ALIVE, i.DEATH, i.CHILD, i.SPOUSE ])
    print("\nIndividuals")
    print(x)
    
    y = PrettyTable()
    y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID',
                    'Husband Name', 'Wife ID', 'Wife Name', 'Children']
    print("Families")  
    #UNCOMMENT 
    # for j in Family_Table.items():
    #     y.add_row([j.ID, j.MARRIED, i.DIVOCED, i.HUSBANDid, 
    #     i.HUSBANDname, i.WIFEid, i.WIFEname, i.CHILDREN])
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
        parser(inputGed)
        table()
    


if __name__ == "__main__": 
    main()
