'''
US 17 - no marriages to children 
'''


def marr2child(famList, famNumber): 
    hubAndChild = []
    err = []
    hubby = []
    for i,x in zip(famList, famNumber): 
        hubAndChild.append(x[0]) #number
        hubAndChild.append(i[3]) #husband
        hubAndChild.append(i[5]) #wife
        hubAndChild.append(i[7:]) #child
        hubby.append(hubAndChild)
        hubAndChild = []

    for i in hubby: 
        for x in i[3]: 
            if i[1] == x: 
                print("ERROR: FAMILY: US17: WIFE MARRIED HER CHILD ON LINE " + str(i[0]))
                err.append("ERROR: FAMILY: US17: WIFE MARRIED HER CHILD ON LINE " + str(i[0]))
            elif i[2] == x: 
                print("ERROR: FAMILY: US17: HUSBAND MARRIED HIS CHILD ON LINE: " + str(i[0]))
                err.append("ERROR: FAMILY: US17: HUSBAND MARRIED HIS CHILD ON LINE: " + str(i[0]))
            else: 
                pass
    for i in err: 
        print(i)
    return err


def main(famLists, famNumber): 
    marr2child(famLists, famNumber)