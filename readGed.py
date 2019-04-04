from prettytable import PrettyTable
from datetime import datetime
import re
import us29, us16, us01, us02, us03, us06, us22, us10, us04, us05, us21, us31, us35, us26, us14, us15, us18, us30, us33, us42, us41, us08, us40, us09, us36, us28
from package.userStories import us07, us32

valid = {
    "0": ("HEAD", "TRLR", "NOTE"),
    "1": ("NAME", "SEX", "BIRT", "DEAT", "DIV", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL"),
    "2": ("DATE")
}

monthWordToInt = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12",
}
# Function to parse through and store families and individuals
def fam(inputGed):
    names = {}
    indi_list = []
    indi_data = []
    fam_list = []
    fam_num = []
    fam_num_list = []
    fam_data = []
    indiv_num = []
    indiv_num_list = []
    new_individual = 0
    new_family = 0
    has_spouse = "False"
    lineNum = 0 
    is_child = "False"
    is_married_date = "False"
    is_divorced = "False"
    birth_year = 0
    for i in inputGed:
        lineNum += 1 
        i = re.sub('[@]', '', i)
        line = i.strip().split(maxsplit=2)
        if line[0] == str(0) and line[1] == "TRLR": 
            if is_married_date != "True": 
                fam_data.insert(1, "NA")
                fam_data.insert(2, "NA") #divorced
                # fam_num.insert(2, "NA")
                # fam_num.insert(3, "NA")
            elif is_married_date == "True" and is_divorced == "False":
                    fam_num.insert(3, "NA")
                    fam_data.insert(2, "NA") #Married but not divorced
            is_married_date = "False"
            is_divorced = "False"

            fam_list.append(fam_data)
            fam_num_list.append(fam_num)

            fam_num = []
            fam_data = []

        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI" and new_individual == 1: #new individual 
                if alive == "False": 
                    indi_data.insert(5, "False")
                    temp = indiv_num[6]
                    indiv_num.insert(7, "")
                    indiv_num[6] = "False"
                    indiv_num[7] = temp
                    if is_child != "True":
                        # indiv_num.append("NA")
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data[8] = "NA"
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")
                elif alive != "False":
                    indiv_num.append("True")
                    indiv_num.append("NA")
                    indi_data.insert(5, "True")
                    indi_data.insert(6, "NA")
                    if is_child != "True":
                        indi_data[7] = "NA"
                        # indiv_num.append("NA")
                        if has_spouse != "True":
                            indi_data.append("NA")
                    else:
                        if has_spouse != "True":
                    
                            indi_data.append("NA")
                indi_list.append(indi_data)
                indiv_num_list.append(indiv_num)
                indiv_num  = []
                indi_data = []

                indiv_num.append(lineNum)
            
                ID_tag = line[1]
                indiv_num.append(line[1])
                indi_data.append(line[1])

                has_spouse = "False"
                is_child = "False"
            elif line[2] == "FAM" and new_family == 1:
                if is_married_date != "True": 
                    fam_data.insert(1, "NA")
                    fam_data.insert(2, "NA") #divorced
                    # fam_num.insert(2, "NA")
                    # fam_num.insert(3, "NA")
                elif is_married_date == "True" and is_divorced == "False":
                    # fam_num.insert(3, "NA")
                    fam_data.insert(2, "NA") #Married but not divorced
                is_married_date = "False"
                is_divorced = "False"
                fam_list.append(fam_data)
                fam_num_list.append(fam_num)

                fam_num = []
                fam_data = []
                fam_num.append(lineNum)
                fam_num.append(line[1])
                fam_data.append(line[1])
            elif line[2] == "INDI" and new_individual == 0: #newly seen indiv
                ID_tag = line[1]
                indiv_num.append(lineNum)
                indiv_num.append(line[1])
                # indi_data.append(lineNum)
                indi_data.append(line[1])
                new_individual = 1
            # Newly Seen Fam
            elif line[2] == "FAM" and new_family == 0:
                if alive == "False":
                    indi_data.insert(5, "False")
        
                    if is_child != "True":
                        # indiv_num.append("NeA")
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data[8] = "NA"
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")
                elif alive != "False": #if they're dead 
                    indiv_num.append("True")
                    indiv_num.append("NA")
                    indi_data.insert(5, "True")
                    indi_data.insert(6, "NA")
                    if is_child != "True": #for the last one 
                        # indiv_num.append("NA")
                        indi_data[7] = "NA"
                        if has_spouse != "True":
                            indi_data.append("NA")
                    else:
                        if has_spouse != "True":
                            indi_data.append("NA")
                indiv_num_list.append(indiv_num)
                indi_list.append(indi_data)
                fam_num.append(lineNum)
                fam_num.append(line[1])
            
                fam_data.append(line[1])
                new_family = 1

        elif line[0] == str(1):
            if line[1] == "NAME":
                NAME_tag = line[2]
                names[ID_tag] = NAME_tag
                indiv_num.append(line[2])
                indi_data.append(line[2])
            elif line[1] == "SEX":
                indiv_num.append(line[2])
                indi_data.append(line[2])
            elif line[1] in ["BIRT", "DEAT", "MARR", "DIV"]:
                date_tag = line[1]
            elif line[1] == "FAMC":
                is_child = "True"
                indi_data.insert(6, "{'" + line[2] + "'}")
                indiv_num.append("{'" + line[2] + "'}")
            elif line[1] == "FAMS":
                has_spouse = "True"
                indi_data.append("{'" + line[2] + "'}")
                indi_data.insert(7, "{'" + line[2] + "'}")
                indiv_num.append("{'" + line[2] + "'}")
                indiv_num.append( "{'" + line[2] + "'}")
            elif line[1] == "HUSB":
                is_married = "True"
                # fam_num.append(line[2])
                fam_data.append(line[2])
            elif line[1] == "WIFE": 
                # fam_num.append(line[2])
                fam_data.append(line[2])
            elif line[1] == "CHIL":
                # fam_num.append("" + line[2] + "")
                fam_data.append("" + line[2] + "")

        elif line[0] == str(2):
            if line[1] == "DATE":
  
                dates = (line[2]).split()
                if date_tag == "BIRT":
                    '''
                    Assumes only error is: 
                    1. Only contains the year i.e. 2 DATE 2032 so it inserts date and month
                    2. Only contains the year and month i.e. 2 DATE NOV 1845 so it inserts date
                    The default for these are day: 01 and month: JAN 
                    '''
                    if len(dates) == 1: #if it only contains the year 
                        # print("Original: " + str(dates))
                        dates.insert(0, '1')
                        dates.insert(1, 'JAN')
                        # print("Revised: " + str(dates))
                    
                    if len(dates) == 2: #if it only contains month and year 
                        # print("Original: " + str(dates))
                        dates.insert(0, '1')
                        # print("Revised: " + str(dates))
                    
                    dates[1] = monthWordToInt[dates[1]]
                    
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    
                    indi_data.append("-".join(dates))
                    indiv_num.append("-".join(dates))
                    current = datetime.now()
                    birth_year = int(dates[0])
                    indi_data.append(current.year - birth_year)
                    indiv_num.append(current.year - birth_year)

                    alive = "True"
                elif date_tag == "DEAT":
                    alive = "False"
                    '''
                    Assumes only error is: 
                    1. Only contains the year i.e. 2 DATE 2032 so it inserts date and month
                    2. Only contains the year and month i.e. 2 DATE NOV 1845 so it inserts date
                    The default for these are day: 01 and month: JAN 
                    '''
                    if len(dates) == 1: #if it only contains the year 
                        # print("Original: " + str(dates))
                        dates.insert(0, '1')
                        dates.insert(1, 'JAN')
                        # print("Revised: " + str(dates))
                    
                    if len(dates) == 2: #if it only contains month and year 
                        # print("Original: " + str(dates))
                        dates.insert(0, '1')
                        # print("Revised: " + str(dates))
                    
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    death_year = int(dates[2])
                    indi_data[4] = death_year - birth_year
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    indiv_num.append("-".join(dates))
                    indi_data.insert(5, "-".join(dates))
                elif date_tag == "MARR": 
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    # fam_num.insert(2, "-".join(dates))
                    fam_data.insert(1, "-".join(dates))
                    is_married_date = "True"
                elif date_tag == "DIV": 
                    dates[1] = monthWordToInt[dates[1]]
                    if (int(dates[0]) < 10):
                        dates[0] = "0" + dates[0]
                    temp = dates[2]
                    dates[2] = dates[0]
                    dates[0] = temp
                    fam_data.insert(2, "-".join(dates))
                    # fam_num.insert(3, "-".join(dates))
                    is_divorced = "True"

    for i in fam_list: 
        if i[3] in names: 
            i.insert(4, names[i[3]])
        if i[5] in names: 
            i.insert(6, names[i[5]])

    # print("-------- Indiv New List -------")
    # for i in indiv_num_list: 
    #     print(i)
    # print("--------Fam New List ---------")
    # for i in fam_num_list: 
    #     print(i)s
    return (indi_list, fam_list, indiv_num_list, fam_num_list)

def table(lists): 
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
                     'Alive', 'Death', 'Child', 'Spouse']

    for i in lists[0]:
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
    print("\nIndividuals")
    print(x)

    y = PrettyTable()
    y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID',
                     'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    print("\nFamilies")
    for j in lists[1]:
        children = "NA"
        if (len(j[6:]) > 0):
            children = "{" + ", ".join(j[7:]) + "}"
        
        y.add_row([j[0], j[1], j[2], j[3], j[4], j[5], j[6], children])
    print(y)

    '''
    Please keep below for visibility of the numbers
    '''
    # z = PrettyTable()
    # z.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age',
    #                  'Alive', 'Death', 'Child', 'Spouse']

    # for i in lists[0]:
    #     z.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8] ])
    # print("\nIndividuals")
    # print(z)

def main():
    try:
        myFile = "Sprint2.ged"
        inputGed = open(myFile, "r")
    except FileNotFoundError:
        print("Cannot open file")
    else:
        allLists = fam(inputGed)
        table(allLists)

        
        individual = us01.main()
        print()
        print("----------Notes----------")
        print()

        us28.orderSiblings(allLists)
        us29.deaths(allLists[0], allLists[2])
        print(us40.main())
        print(us41.main())
        recentBirthList = us35.RecentBirths(individual)
        if len(recentBirthList) > 0:
            for i in recentBirthList:
                print("NOTIFICATION: INDIVIDUAL: US35: "+ i + ": Birthday " + individual[i].birthDate + " was born in the last 30 days")
        
        print()
        print('----------Individual Errors----------')
        print()

        for indi in individual:
            us01Test_Birth = us01.BirthBeforeCurrent(indi)
            if us01Test_Birth !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Birthday " + individual[indi].birthDate + " occurs in the future")
            us01Test_Death = us01.DeathBeforeCurrent(indi)
            if us01Test_Death !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Death date " + individual[indi].deathDate + " occurs in the future")
            us01Test_Marriage = us01.MarriageBeforeCurrent(indi)
            if us01Test_Marriage !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Marriage date " + individual[indi].marriageDate + " occurs in the future")
            us01Test_Divorce = us01.DivorceBeforeCurrent(indi)
            if us01Test_Divorce !=  True:
                print("ERROR: INDIVIDUAL: US01: "+ individual[indi].ID + ": Divorce date " + individual[indi].divorceDate + " occurs in the future")
            us02Test = us02.BirthBeforeMarriage(individual[indi])
            if us02Test != True:
                print("ERROR: INDIVIDUAL: US02: "+ individual[indi].ID + ": Birthday " + individual[indi].birthDate + " occurs before marriage " + individual[indi].marriageDate)
        
        us07.main(allLists[0], allLists[2])
        us16.sameLastName(allLists[0], allLists[2])
        us32.main(allLists[2])

        print()
        print("------------Family Errors------------")
        print()
        
        us14.main(allLists[0], allLists[1], allLists[3])
        us26.corrEntries(allLists)
        us15.main(allLists[1], allLists[2])
        us03.main(allLists[0])
        us04.main(allLists[1])

        print()
        print("------------Individual and Family Errors------------")
        print()
       
        us22.uniqueIDs(allLists)
        us42.filterDates(allLists)
        # us05.main(allLists[0], allLists[1])
        # us06.main(allLists[0], allLists[1])  
        # us07.main(allLists[0])
        
        # us10.main(allLists[0], allLists[1])
 
        
        # us18.main(allLists[1])
        
        # family = us21.main()
        # for i in family:
        #     if us21.CheckGenderForRole(i) != True:
        #         print("ERROR: FAMILY: US21: " + family[i].ID + ": gender was wrong")
        
        # us30.checkForLivingMarried(allLists[0])
        # us31.checkForLivingSingle(allLists[0])
        
        # us33.checkForOrphan(allLists[0], allLists[1])
        # us36.main(allLists[2]
        # input2 = open(myFile, "r")
        # us40.main(input2)
        # input2.close()

        # familyInfo = us08.main()
        # for index in familyInfo:
        #     for child in familyInfo[index].children:
        #         if us08.BirthBeforeMarriageOfParents(index, child) != True:
        #             print("ERROR: FAMILY: US08: " + familyInfo[index].ID + ":" + child  + ": Children born before marriage of parents or more than 9 months after their divorce")
        
        
        # for index in familyInfo:
        #     for child in familyInfo[index].children:
        #         if us08.BirthBeforeMarriageOfParents(index, child) != True:
        #             print("ERROR: FAMILY: US09: " + familyInfo[index].ID + ":" + child  + ": Children born after death of mother or after 9 months after death of father")
        

        print("\n")
if __name__ == "__main__":
    main()