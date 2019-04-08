'''
User Story 35
List recent births

'''
from datetime import date, datetime
import us01


def RecentBirths(individual):
    recentBirthID = []
    for indi in individual:
        if individual[indi].birthDate != 'NA':
            birthdate = individual[indi].birthDate
            today = date.today().strftime("%Y-%m-%d")
            todayDate = datetime.strptime(today, "%Y-%m-%d")
            try:
                birthDate = datetime.strptime(birthdate, "%Y-%m-%d")
            except ValueError:
                birthDate = datetime.strptime("2018-01-01", "%Y-%m-%d")
            diffDate = (todayDate - birthDate)

            if diffDate.days < 30 and diffDate.days > 0:
                recentBirthID.append(indi)
    return recentBirthID


def main():
    result = us01.main()
    individual = result[0]
    return individual
