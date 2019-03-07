'''
Unit Test for US14
No more than 5 siblings should be born at the same time 
'''
def checkForMoreThan5Sibs(indiv, fam): 
        bdays = {}
        family = []
        sibs = []
        full = []
        bdy_temp = 0
        num = 0
        days = []
        res = []
        for i in indiv: 
                 bdays[i[0]] = i[3]
        for i in fam: 
                sibs.append(i[7:])
                family.append(i[0])
        for i in sibs: 
                for j in i: 
                        if j in bdays: 
                                days.append(int(bdays.get(j).split("-")[0]))
                full.append(days)
                days = []
        for i in full: 
                num += 1
                for b in i: 
                        count = i.count(b)
                        if count > 5: 
                                print("ERROR: FAMILY: US14: "+ str(family[num]) + " MORE THAN 5 SIBLINGS HAVE MULTIPLE BIRTHDAYS ON YEAR " + str(b))
                                res.append("ERROR: FAMILY: US14: "+ str(family[num]) + " MORE THAN 5 SIBLINGS HAVE MULTIPLE BIRTHDAYS ON YEAR " + str(b))
                                break
                              
        return res

def main(lists1, list2): 
        return checkForMoreThan5Sibs(lists1, list2)