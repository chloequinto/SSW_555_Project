'''
US - 15: Fewer than 15 siblings 
'''
def checkFewerThan15(input):
    for i in input: 
        if len(i) >= 21: 
            print("ERROR: FAMILY: US15: " + i[0] + " has more than 15 " )



def main(lists): 
    checkFewerThan15(lists)