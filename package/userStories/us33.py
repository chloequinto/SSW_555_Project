'''
US31 - List Orphans
'''
import readGed

def checkForOrphan(inputIndi, inputFam, newFam):
    orphans = []
    Families = []
    MomID = "Null"
    DadID = "Null"
    MotherDeceased = False
    FatherDeceased = False
    for i, b in zip(inputIndi, newFam):  
        if i[7] != "NA":
            Families.append(i[7][2] + i[7][3])

    for j in inputFam:
        if j[0] in Families:
            MomID = j[5]
            DadID = j[3]
            

    for k in inputIndi:
        if k[0] == MomID and k[5] == "False":
            MotherDeceased = True
        if k[0] == DadID and k[5] == "False":
            FatherDeceased = True
        if MotherDeceased == True and FatherDeceased == True:
            fixString = "NOTE: US33: Individual " + i[0] + " is an orphan"
            if fixString not in orphans:
                print("NOTE: US33: Individual " + i[0] + " is an orphan on line " + str(b[0]))
                orphans.append("NOTE: US33: Individual " + i[0] + " is an orphan")
    return orphans

def main(inputIndi, inputFam, newFam):
    checkForOrphan(inputIndi, inputFam, newFam)