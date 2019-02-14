'''
User Story 32
List Multiple Births 
'''
import collections 

def checkMultipleBirths(inputGed):
    births = []
    people = {}
    family = {}
    if inputGed == "": 
        return []
    for i in inputGed: 
        line = i.strip().split(maxsplit=2)
        if len(line) > 2 and line[0] == str(0):
            if line[2] == "INDI": 
                name = line[1] 
            elif line[2] == "FAM":
                famId = line[1] 
        elif line[1] == "BIRT": 
            tag = line[1]
        elif line[0] == str(2) and line[1] == "DATE": 
            if tag == "BIRT": 
                people[line[2]] = name 
                births.append(line[2])
        # elif line[1] == "HUSB": 
        #     family[famId] = line[2]
        # elif line[1] == "WIFE": 
        #     family.append(line[2])
        # elif line[1] == "CHIL": 
        #     family[famId].append(line[2])
    # print(people)
    # print(family)
    date = [item for item, count in collections.Counter(births).items() if count > 1]
    if date == []: 
        return "No multiple births found"
    for i in date: 
        return "Fam: " + "experienced multiple birth dates on " + str(i)

    

def main(): 
    try: 
        inputGed = open("input.ged", "r")
        inputGed1 = open("input_2.ged", "r")
        inputGed2 = open("input_3.ged", "r")
        
    except FileNotFoundError:
        print("Can't open the file")
    else:
        print(checkMultipleBirths(inputGed2))


if __name__ == "__main__":
    main()