import re
from datetime import datetime
import us40


def checkForLessThan150(lists, listNum): 
    today = datetime.today()
    year = today.year
    res = []

    for i, x in zip(lists, listNum): 
        if i[5] == str(True): #if they're alive 
            birthday = i[3]
            if (year - int(birthday.split('-')[0]) > 150):
                print("ERROR: INDIVIDUAL: US07: " + i[0] + " is older than 150 line " + str(x[0]))
                res.append("ERROR: INDIVIDUAL: US07: " + i[0] + " is older than 150 line " + str(x[0]))
        else: #if they're dead
            birth = i[3]
            death = i[6]
            if(int(death.split("-")[0]) - int(birth.split("-")[0]) > 150 ): 
                print("ERROR: INDIVIDUAL: US07: " + i[0] + " death - birth > 150 line " + str(x[0]))
                res.append("ERROR: INDIVIDUAL: US07: " + i[0] + " death - birth > 150 line " + str(x[0]))
    return res

        

def main(lists, listNum): 
    checkForLessThan150(lists, listNum)
