'''
US - 15: Fewer than 15 siblings 
'''
def checkFewerThan15(input):
    res = []
    print("ERROR: FAMILY: US15: " +  str(any(len(i) > 21 for i in input if True)) + " a family has more than 15 siblings")
    res.append("ERROR: FAMILY: US15: " +  str(any(len(i) > 21 for i in input if True)) + " a family has more than 15 siblings")
    return res

 

def main(lists): 
    checkFewerThan15(lists)