'''
User Story 23
Unique name and birthday
'''

def uniqueNameAndBirthday(input, lineNum):
        indivs = []
        errors = []
        for i, b in zip(input, lineNum):
                person = []
                if i[1] != "NA":
                        person.append(i[1])
                if i[3] != "NA":
                        person.append(i[3])
                if person in indivs:
                        print("ERROR: INDIVIDUAL: US23: " + i[0] + " does not have a unique name and birthday on line: " + str(b[0]))
                        errors.append("ERROR: INDIVIDUAL: US23: " + i[0] + " does not have a unique name and birthday on line: " + str(b[0]))
                else:
                        indivs.append(person)
        return errors

def main(input, lineNum):
        uniqueNameAndBirthday(input, lineNum)

     



        