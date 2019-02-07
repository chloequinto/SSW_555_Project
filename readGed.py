'''To Do 
1. Check that it works 
2. Try and Exception for inputs 
3. Test 
'''

valid = {
    "0": ("HEAD", "TRLR", "NOTE"),
    "1": ("NAME", "SEX", "BIRT", "DEAT", "DIV", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL"),
    "2": ("DATE")
}

inputGed = open("GEDCOM.ged", "r")

writeOutput = open("output.txt", "w")

print("Opening files")

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