'''
US31 - Lists living single
'''


def checkForLivingSingle(input): 
    errors = []
    for i in input: 
        if i[5] == "True":
            if i[8] == "NA": 
                print("ERROR: INDIVIDUAL: US31 " + i[0] + " " + i[1] +  " is living and single")
                errors.append("ERROR: INDIVIDUAL: US31 " + i[0] + " " + i[1] +  " is living and single")
    print(errors)

def main(lists):
    checkForLivingSingle(lists) 



