'''
User Story 09
Birth before death of parents

'''

from datetime import date
from datetime import datetime, timedelta
import us01


def BirthBeforeDeathOfParents(fam, indi, individual):
    mom = fam.wife
    dad = fam.husband
    if individual[mom].deathDate != 'NA':
        us01.checkDate(indi.birthDate, individual[mom].deathDate)
    elif individual[dad].deathDate != 'NA':
        try:
            death = datetime.strptime(individual[dad].deathDate, "%Y-%m-%d")
        except ValueError:
            death = datetime.strptime("2018-01-01", "%Y-%m-%d")

        try:
            birthDate = datetime.strptime(indi.birthDate, "%Y-%m-%d")
        except ValueError:
            birthDate = datetime.strptime("2018-01-01", "%Y-%m-%d")

        diffDate = birthDate - death
        if diffDate.days > 273:
            return False
    return True


def main():
    result = us01.main()
    family = result[1]
    return family
