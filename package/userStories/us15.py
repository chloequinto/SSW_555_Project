'''
US - 15: Fewer than 15 siblings 
'''
def checkFewerThan15(input, input2):
    res = []
    val  = any(len(i) > 21 for i in input if True)
    for i, b in zip(input,input2): 
        if len(i) > 21: 
            print("ERROR: FAMILY: US15: " +  str(val) + " "+ str(b[1]) +" family has more than 15 siblings line " + str(b[0]))
            res.append("ERROR: FAMILY: US15: " +  str(val)+ " "+ str(b[1]) +" family has more than 15 siblings line " + str(b[0]))
    return res

 

def main(lists, list2): 
    checkFewerThan15(lists, list2)