'''To Do 
1. Check that it works 
2. Try and Exception for inputs [x] 
3. 
4. 
5. 
6. Unit Tests 
'''

valid = {
    "0": ("HEAD", "TRLR", "NOTE"),
    "1": ("NAME", "SEX", "BIRT", "DEAT", "DIV", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL"),
    "2": ("DATE")
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

def main(): 
    global inputGed, writeOutput
    try:
        inputGed = open("input.ged", "r")
        writeOutput = open("output.txt", "w")

        print("Opening files")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        parser(inputGed)


if __name__ == "__main__": 
    main()
