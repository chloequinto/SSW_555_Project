'''
User Story 30
List living married

'''
import readGed

def checkForLivingMarried(input): 
    notes = []
    for i, j in zip(input[0], input[2]): 
        if i[5] == "True":
            if i[8] != "NA": 
                print("NOTE: INDIVIDUAL: US30: " + i[0] + " " + i[1] +  " is living and married on line " + str(j[0]))
                notes.append("NOTE: INDIVIDUAL: US30: " + i[0] + " " + i[1] +  " is living and married on line " + str(j[0]))
    return notes

def main(lists):
    checkForLivingMarried(lists)