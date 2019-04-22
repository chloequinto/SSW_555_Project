'''
US31 - List Orphans
'''
import readGed

def checkForOrphan(inputIndi, inputFam, newFam):
    orphans = []
    Families = []
    parents = []
    MomID = "Null"
    DadID = "Null"
    for i, b in zip(inputIndi, newFam): 
        if i[7] != "NA":
            yes = len(i[7])
            if yes <= 6:
                Families.append(i[7][2] + i[7][3])
            else:
                Families.append(i[7][2] + i[7][3]+ i[7][4]) 

    for j in inputFam:
        if j[0] in Families:
            MomID = j[5]
            DadID = j[3]
            MotherDeceased = False
            FatherDeceased = False
                

        for k in inputIndi:
            if k[0] == MomID and k[5] == "False":
                MotherDeceased = True
            if k[0] == DadID and k[5] == "False":
                FatherDeceased = True
            if MotherDeceased == True and FatherDeceased == True:
                if MomID not in parents:
                    parents.append(MomID)
                if DadID not in parents:
                    parents.append(DadID)
    for l in inputFam:
        if l[3] in parents and l[5] in parents:
            if len(i) > 7:
                children = []
                children.append(l[7:])
                for g in children:
                    fixString = "NOTE: US33: Individual " + g[0] + " is an orphan"
                    if fixString not in orphans:
                        print("NOTE: US33: Individual " + g[0] + " is an orphan on line " + str(b[0]))
                        orphans.append("NOTE: US33: Individual " + g[0] + " is an orphan")
                    
    return orphans

def main(inputIndi, inputFam, newFam):
    checkForOrphan(inputIndi, inputFam, newFam)