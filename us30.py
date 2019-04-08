'''
User Story 30
List living married

'''
import readGed

def checkForLivingMarried(input): 
    errors = []
    for i in input: 
        if i[5] == "True":
            if i[8] != "NA": 
                print("ERROR: INDIVIDUAL: US30: " + i[0] + " " + i[1] +  " is living and married")
                errors.append("ERROR: INDIVIDUAL: US30: " + i[0] + " " + i[1] +  " is living and married")
    return errors

def main(lists):
    checkForLivingMarried(lists)