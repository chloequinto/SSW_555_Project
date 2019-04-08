'''
User Story 21
Correct gender for role

'''

from package.userStories import us01


def CheckGenderForRole(fam, individual):
    husband = fam.getHusband()
    wife = fam.getWife()
    if(individual[husband].getSex() != 'M'):
        return False
    if(individual[wife].getSex() != 'F'):
        return False
    else:
        return True


def main():
    result = us01.main()
    family = result[1]
    return family
