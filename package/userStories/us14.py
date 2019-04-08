'''
Unit Test for US14
No more than 5 siblings should be born at the same time 
'''

family = []
sibs  = [] 
bdays = {}

def checkForMoreThan5Sibs(indiv, fam, fam2): 
        global family, sibs, bdays
        full = []
        num = 0
        days = []
        res = []
        formats(indiv, fam)
        for i in sibs: 
                for j in i: 
                        if j in bdays: 
                                days.append(int(bdays.get(j).split("-")[0]))
                full.append(days)
                days = []

        for i in full: 
                num += 1 #count which family 
                for b in i: 
                        count = i.count(b)
                        if count > 5: 
                                print("ERROR: FAMILY: US14: "+ str(family[num]) +  " more than 5 siblings have multiple birthdays on year " + str(b) + " line " + str(fam2[num][0]))
                                res.append("ERROR: FAMILY: US14: "+ str(family[num]) + " more than 5 siblings have multiple birthdays on year " + str(b) + " line " + str(fam2[num][0]))
                                break
             
        return res

def formats(indiv, fam): 
        global family, sibs, bdays
        for i in indiv: 
                bdays[i[0]] = i[3]
        for i in fam: 
                sibs.append(i[7:])
                family.append(i[0])

def main(lists1, list2, list3): 
        return checkForMoreThan5Sibs(lists1, list2, list3)