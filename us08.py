'''
User Story 08
Birth before marriage of parents

'''

from datetime import date, datetime, timedelta
import us01


def BirthBeforeMarriageOfParents(fam, indi):
    if indi.birthDate != 'NA' and fam.marriageDate != 'NA':
        firstCheck = us01.checkDate(fam.marriageDate, indi.birthDate)
        if fam.divorceDate != 'NA':
            try:
                divorceDate = datetime.strptime(fam.divorceDate, "%Y-%m-%d")
            except ValueError:
                divorceDate = datetime.strptime("2018-01-01", "%Y-%m-%d")

            try:
                birthDate = datetime.strptime(indi.birthDate, "%Y-%m-%d")
            except ValueError:
                birthDate = datetime.strptime("2018-01-01", "%Y-%m-%d")

            diffDate = birthDate - divorceDate
            secondCheck = True
            if diffDate.days > 273:
                secondCheck = False
            result = firstCheck and secondCheck
            return result
        else:
            return firstCheck

    elif indi.birthDate == 'NA':
        return True
    elif fam.marriageDate == 'NA':
        return True
    elif fam.divorceDate == 'NA':
        return True


def main():
    result = us01.main()
    family = result[1]
    return family
