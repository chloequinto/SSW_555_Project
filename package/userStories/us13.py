'''
User Story 13
Siblings spacing

Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''
from datetime import date, datetime
from package.userStories import us01


def SiblingsSpacing(family, individual):
    children = family.children
    siblings = []
    res = True

    if len(children) > 1:
        for i in children:
            for j in children:
                if i != j:
                    try:
                        if i in individual and individual[i].birthDate != 'NA':
                            birth1 = datetime.strptime(
                                individual[i].birthDate, "%Y-%m-%d")
                        else:
                            continue

                        if j in individual and individual[j].birthDate != 'NA':
                            birth2 = datetime.strptime(
                                individual[j].birthDate, "%Y-%m-%d")
                        else:
                            continue
                    except ValueError:
                        birth1 = datetime.strptime("2018-01-01", "%Y-%m-%d")
                        birth2 = datetime.strptime("2018-01-01", "%Y-%m-%d")

                    diffDate = abs(birth1 - birth2)
                    if diffDate.days < 2 or diffDate.days > 240:
                        continue
                    else:
                        if i not in siblings:
                            siblings.append(i)
                        if j not in siblings:
                            siblings.append(j)
                        res = False
                
    return (res, siblings)


def main():
    result = us01.main()
    individual = result[0]
    family = result[1]
    return individual
