'''
US31 - Lists living single
'''
import readGed

def checkForLivingSingle(input, lineNum): 
    errors = []
    for i, x in zip(input,lineNum): 
        if i[5] == "True":
            if i[8] == "NA": 
                print(f"ERROR: INDIVIDUAL: US31: {i[0]}  {i[1]} on line: {x[0]} is living and single")
                errors.append(f"ERROR: INDIVIDUAL: US31: {i[0]} {i[1]} on line: {x[0]} is living and single")
    return errors

def main(lists, lineNum):
    checkForLivingSingle(lists, lineNum)

    
     



