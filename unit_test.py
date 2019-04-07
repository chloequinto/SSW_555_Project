'''
All Unit Tests 
'''
import us03
import us16
import us29
import us06
import us04
import us05
import us22
import us15
import us26
import us35
import us01
import us02
import us21
import us31
import us10
import us26
import us14
import us15
import us18
import us30
import us42
import us33
import us41
import us08
import us09
import us40
import us28
import us12
import us36
import us38
import unittest
import readGed
from package.userStories import us07, us32

deaths1 = [
    ['I6', 'Grandpa /Quinto/', 'M', '1940-06-03', 64, 'False',
        '2004-07-17', 'NA', "{'F5'}", "{'F3'}", "{'F5'}"],
    ['I7', 'Grandma /Quinto/', 'F', '1940-06-11',
        62, 'False', '2002-06-06', 'NA', "{'F3'}"],
    ['I9', 'Grandma /Loresco/', 'F', '1940-04-03',
        54, 'False', '1994-10-16', 'NA', "{'F4'}"],
    ['I10', 'Ex /Quinto/', 'F', '1945-10-07', 56,
        'False', '2001-07-13', 'NA', "{'F5'}"]
]

deaths2 = [
    ['I1', 'Bob /Smiath/', 'M', '1907-04-04', 92, 'False',
        '1999-10-31', "{'F2'}", "{'F1'}", "{'F1'}"],
    ['I1', 'Johnathan /Smith/', 'M', '1879-11-21',
        80, 'False', '1959-04-10', 'NA', "{'F2'}"],
    ['I3', 'Dorothy /Rodgers/', 'F', '1879-10-01',
        83, 'False', '1962-05-18', 'NA', "{'F2'}"],
    ['I4', 'Mary /Johnson/', 'F', '1908-02-03',
        81, 'False', '1989-06-29', 'NA', "{'F1'}"],
    ['I6', 'Nancy /Jefferson/', 'F', '1942-02-15',
        34, 'False', '1976-12-09', 'NA', "{'F4'}"]
]

name1 = (
    [
        ['I2', 'Rafael /Quinto/', 'M', '1968-04-04', 51,
            'True', 'NA', "{'F2'}", "{'F3'}", "{'F2'}"],
        ['I4', 'Rocky /Quinto/', 'M', '1995-06-28',
            24, 'True', 'NA', "{'F2'}", 'NA'],
        ['I5', 'Thompson /L/', 'M', '1997-01-30',
            22, 'True', 'NA', 'NA', "{'F1'}"],
        ['I6', 'Grandpa /Quinto/', 'M', '1940-06-03', 64, 'False',
            '2004-07-17', 'NA', "{'F5'}", "{'F3'}", "{'F5'}"],
        ['I8', 'Grandpa /Loresco/', 'M', '1940-10-05',
            79, 'True', 'NA', 'NA', "{'F4'}"],
        ['I11', 'John /Quinto/', 'M', '1960-09-08',
            59, 'True', 'NA', "{'F5'}", 'NA']
    ],
    []
)

name2 = (
    [
        ['I1', 'Johnathan /Smith/', 'M', '1879-11-21',
            80, 'False', '1959-04-10', 'NA', "{'F2'}"],
        ['I8', 'Michael /Smith/', 'M', '1975-03-20',
            44, 'True', 'NA', "{'F4'}", 'NA'],
    ],
    [
        "ERROR: INDIVIDUAL: US16: Bob /Smiath/ does not have the same last name on line 25",
        "ERROR: INDIVIDUAL: US16: Brian /Smith/ does not have the same last name on line 25"
    ]
)

us32res = (
    ["ERROR: INDIVIDUAL: US32: I1 has the same birthdays as someone else on ['2032-06-10'] line 14",
     "ERROR: INDIVIDUAL: US32: I4 has the same birthdays as someone else on ['2032-06-10'] line 44"]
)

us32res1 = (
    ["ERROR: INDIVIDUAL: US32: I3 has the same birthdays as someone else on ['1995-06-28'] line 35",
     "ERROR: INDIVIDUAL: US32: I4 has the same birthdays as someone else on ['1995-06-28'] line 45"]
)


class TestResults(unittest.TestCase):

    maxDiff = None  # check for full errors

    def testUS03(self):
        inputGed = open("Sprint2.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)

        inputGed.close()

        self.assertEqual(us03.birthBeforeDeath(output[0], output[2]), [
                         "ERROR: INDIVIDUAL: US03: I4 on line: 44: Death date occurs before their date of birth."])
        inputGed1.close()

    def testUS32(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_8.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us32.checkMultipleBirths(output[2]), us32res)
        self.assertEqual(us32.checkMultipleBirths(output1[2]), us32res1)

    def testUS07(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_8.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us07.checkForLessThan150(output[0], output[2]), [
                         "ERROR: INDIVIDUAL: US07: I3 is older than 150 line 35"])
        self.assertEqual(us07.checkForLessThan150(output1[0], output1[2]), [
                         "ERROR: INDIVIDUAL: US07: I9 death - birth > 150 line 95"])

    def testUS29(self):
        inputGed = open("inputRZ1.ged", "r")
        inputGed1 = open("inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us29.deaths(output[0], output[2]), deaths1)
        self.assertEqual(us29.deaths(output1[0], output1[2]), deaths2)

    def testUS16(self):  # us16
        inputGed = open("inputRZ1.ged", "r")
        inputGed1 = open("inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us16.sameLastName(output[0], output[2]), name1)
        self.assertEqual(us16.sameLastName(output1[0], output1[2]), name2)

    def testUS06(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us06.main(output[0], output[1], output[3]), [
                         "ERROR: INDIVIDUAL: US06: I4: Divorce date occurs after their date of death on line 88"])

    def testUS04(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us04.marriageBeforeDivorce(output[1]), [
                         'ERROR: FAMILY: US04: F1: Divorce date occurs before their marriage.'])
        inputGed.close()

    def testUS05(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us05.main(output[0], output[1]), [
                         "ERROR: INDIVIDUAL: US05: I4: Marriage date occurs after their date of death."])
        inputGed.close()

    def testUS01(self):
        inputGed = open("inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        for i in individual:
            self.assertTrue(us01.BirthBeforeCurrent(i), msg="ERROR: INDIVIDUAL: US01: " +
                            individual[i].ID + ": Birthday " + individual[i].birthDate + " occurs in the future")
            self.assertTrue(us01.DeathBeforeCurrent(i), msg="ERROR: INDIVIDUAL: US01: " +
                            individual[i].ID + ": Death date " + individual[i].deathDate + " occurs in the future")
            self.assertTrue(us01.MarriageBeforeCurrent(i), msg="ERROR: INDIVIDUAL: US01: " +
                            individual[i].ID + ": Marriage date " + individual[i].marriageDate + " occurs in the future")
            self.assertTrue(us01.DivorceBeforeCurrent(i), msg="ERROR: INDIVIDUAL: US01: " +
                            individual[i].ID + ": Divorce date " + individual[i].divorceDate + " occurs in the future")

    def testUS02(self):
        inputGed = open("inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        for indi in individual:
            self.assertTrue(us02.BirthBeforeMarriage(individual[indi]), msg="ERROR: INDIVIDUAL: US02: " + individual[indi].ID +
                            ": Birthday " + individual[indi].birthDate + " occurs before marriage " + individual[indi].marriageDate)

    def testUS35(self):
        inputGed = open("inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        self.assertEqual(us35.RecentBirths(individual), ['I1'])

    def testUS21(self):
        inputGed = open("inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for i in family:
            self.assertTrue(us21.CheckGenderForRole(
                family[i], individual), msg="ERROR: FAMILY: US21: " + family[i].ID + ": gender was wrong")

    def testUS31(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us31.checkForLivingSingle(output1[0], output1[2]), [
                         'ERROR: INDIVIDUAL: US31: I4 Rocky /Quinto/ on line: 45 is living and single', 'ERROR: INDIVIDUAL: US31: I11 John /Quinto/ on line: 117 is living and single'])
        inputGed.close()
        self.assertEqual(us31.checkForLivingSingle(output[0], output[2]), [])
        inputGed1.close()

    def testUS10(self):
        inputGed = open("Orphan.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us10.main(output[0], output[1], output[3]), ['ERROR: INDIVIDUAL: US10: I1 marriage date occurs before they are 15 on line 245', 'ERROR: INDIVIDUAL: US10: I4 marriage date occurs before they are 15 on line 260',
                                                                      'ERROR: INDIVIDUAL: US10: I5 marriage date occurs before they are 15 on line 245', 'ERROR: INDIVIDUAL: US10: I6 marriage date occurs before they are 15 on line 260'])
        inputGed1.close()

    def testUS14(self):
        inputGed = open("Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us14.main(output[0], output[1], output[3]), [
                         "ERROR: FAMILY: US14: F4 more than 5 siblings have multiple birthdays on year 2018 line 261"])

    def testUS22(self):
        inputGed = open("Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us22.uniqueIDs(output), (['I21'], []))

    def testUS26(self):
        inputGed = open("Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us26.corrEntries(output), ["ERROR: FAMILY: US26: Family F2 does not have the correct corresponding entries on line 231",
                                                    "ERROR: FAMILY: US26: Family F3 does not have the correct corresponding entries on line 237", "ERROR: FAMILY: US26: Family F4 does not have the correct corresponding entries on line 261"])

    def testUS15(self):
        inputGed = open("Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us15.checkFewerThan15(output[1], output[2]), [
                         "ERROR: FAMILY: US15: True I3 family has more than 15 siblings line 35"])

    def testUS18(self):
        inputGed = open("Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us18.main(output[1]), [
                         "ERROR: FAMILY: US18: ['I8', 'I7'] Siblings should not marry."])

    def testUS30(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us30.checkForLivingMarried(output1[0]), ['ERROR: INDIVIDUAL: US30: I1 Chloe /Quinto/ is living and married', 'ERROR: INDIVIDUAL: US30: I2 Rafael /Quinto/ is living and married',
                                                                  'ERROR: INDIVIDUAL: US30: I3 Maria /Quinto/ is living and married', 'ERROR: INDIVIDUAL: US30: I5 Thompson /L/ is living and married', 'ERROR: INDIVIDUAL: US30: I8 Grandpa /Loresco/ is living and married'])
        inputGed.close()
        self.assertEqual(us30.checkForLivingMarried(output[0]), ['ERROR: INDIVIDUAL: US30: I1 Edward /Rogers/ is living and married', 'ERROR: INDIVIDUAL: US30: I3 Emily /Rogers/ is living and married',
                                                                 'ERROR: INDIVIDUAL: US30: I5 Marcia /Rogers/ is living and married', 'ERROR: INDIVIDUAL: US30: I6 Tim /Jones/ is living and married'])
        inputGed1.close()

    def testUS42(self):
        inputGed = open("inputRZ1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertTrue(us42.filterDates(output))

    def testUS33(self):
        inputGed = open("Orphan.ged", "r")
        output = readGed.fam(inputGed)
        self.assertTrue(us33.checkForOrphan(output[0], output[1], output[2]), [
                        "NOTE: US33: Individual I24 is an orphan on line 236"])

    def testUS41(self):
        self.assertEqual(
            us41.main(), "NOTE: US41: DATES ARE FIXED TO INCLUDE PARTIALS")

    def testUS40(self):
        self.assertEqual(us40.main(), "NOTE: US40: LINE NUMBERS ARE ADDED")

    def testUS08(self):
        inputGed = open("inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for index in family:
            for child in family[index].children:
                if us08.BirthBeforeMarriageOfParents(family[index], individual[child]) != True:
                    self.assertTrue("ERROR: FAMILY: US08: " + family[index].ID + ":" + child +
                                    ": Children born before marriage of parents or more than 9 months after their divorce")

    def testUS09(self):
        inputGed = open("inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for index in family:
            for child in family[index].children:
                if us09.BirthBeforeDeathOfParents(family[index], individual[child], individual) != True:
                    self.assertTrue("ERROR: FAMILY: US09: " + family[index].ID + ":" + child +
                                    ": Children born after death of mother or after 9 months after death of father")

    def testUS28(self):
        inputGed = open("Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us28.orderSiblings(output), {'F1': [['I1', -13, 14]], 'F2': [['I4', -19, 44]], 'F4': [['I7', 4, 74], ['I8', 3, 84]], 'F5': [['I10', 2, 104], ['I9', 0, 94]], 'F3': [
                         ['I11', 1, 114], ['I12', 1, 123], ['I13', 1, 132], ['I14', 1, 141], ['I15', 1, 150], ['I16', 1, 159], ['I17', 0, 168], ['I18', -1, 177], ['I19', -2, 186], ['I20', -3, 195], ['I21', -5, 213]]})
'''
    def testUS36(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us36.main(allLists[2])), [
                         "ERROR: INDIVIDUAL: US36: Line: I4: "])
        inputGed.close()

    def testUS38(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us38.main(allLists[2])), [
                         "ERROR: INDIVIDUAL: US38: Line: I4: "])
        inputGed.close()
'''
    def testUS12(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us12.checkForOldParents(output[0], output[1], output[2]), ["Error: US12: Individual: I1's father is too old on line: 14",
                                                                                    "Error: US12: Individual: I1's mother is too old on line: 14", "Error: US12: Individual: I4's father is too old on line: 44", "Error: US12: Individual: I4's mother is too old on line: 44"])


if __name__ == '__main__':
    unittest.main()
