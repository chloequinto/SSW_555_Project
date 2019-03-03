# User Story 7 

import re
from datetime import datetime



def checkForLessThan150(lists): 
    today = datetime.today()
    year = today.year
    res = []
    for i in lists: 
        if i[5] == str(True): #if they're alive 
            birthday = i[3]
            if (year - int(birthday.split('-')[0]) > 150):
                print("ERROR: INDIVIDUAL: US07: " + i[0] + " is older than 150")
                res.append("ERROR: INDIVIDUAL: US07: " + i[0] + " is older than 150")
        else: #if they're dead
            birth = i[3]
            death = i[6]
            if(int(death.split("-")[0]) - int(birth.split("-")[0]) > 150 ): 
                print("ERROR: INDIVIDUAL: US07: " + i[0] + " death - birth > 150")
                res.append("ERROR: INDIVIDUAL: US07: " + i[0] + " death - birth > 150")


        



def main(lists): 
    checkForLessThan150(lists)
