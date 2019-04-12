'''
User Story 20
Aunts and uncles

Aunts and uncles should not marry their nieces or nephews
'''
from package.userStories import us01


def getAllChildren(family):
    children = family.children
    return children


def NotMarryNiecesAndNephews(fam, family, individual):
    wife = fam.wife
    husband = fam.husband
    wifeSiblings = []
    husbandSiblings = []
    wifeFam = individual[wife].childIdentity
    husbandFam = individual[husband].childIdentity
    if wifeFam != 'NA':
        wifeSiblings = getAllChildren(family[wifeFam])
    if husbandFam != 'NA':
        husbandSiblings = getAllChildren(family[husbandFam])
    error = []
    res = True
    if husbandFam != 'NA' and family[husbandFam].wife != 'NA' and family[husbandFam].wife in wifeSiblings:
        error.append(fam)
        res = False
    elif husbandFam != 'NA' and family[husbandFam].husband != 'NA' and family[husbandFam].husband in wifeSiblings:
        error.append(fam)
        res = False
    elif wifeFam != 'NA' and family[wifeFam].wife != 'NA' and family[wifeFam].wife in husbandSiblings:
        error.append(fam)
        res = False
    elif wifeFam != 'NA' and family[wifeFam].husband != 'NA' and family[wifeFam].husband in husbandSiblings:
        error.append(fam)
        res = False

    return (res, error)


def main():
    result = us01.main()
    individual = result[0]
    return individual
