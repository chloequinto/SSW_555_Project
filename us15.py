'''
US - 15: Fewer than 15 siblings 
'''
def checkFewerThan15(input):
    problem = False
    errors = []
    for i in input: 
        if len(i) >= 21: 
            problem = True
            
            errors.append("ERROR: FAMILY: US15: " + i[0] + " has more than 15 siblings.")
    if problem == True: 
        for i in errors: 
            print(str(i))
    return errors

def main(lists): 
    checkFewerThan15(lists)