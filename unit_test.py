'''
All Unit Tests 
'''

from package.userStories import us01, us02, us03, us04, us05, us06, us07, us08, us09, us10, us12, us13, us14, us15, us16, us17, us18, us21, us22, us23, us24, us25, us26, us27, us28, us29, us30, us31, us32, us33, us34, us35, us36, us38, us40, us41, us42, us20, us39, us37
import unittest
import readGed

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
        inputGed = open("data/Sprint2.ged", "r")
        inputGed1 = open("data/input_6.ged", "r")
        output = readGed.fam(inputGed)

        inputGed.close()

        self.assertEqual(us03.birthBeforeDeath(output[0], output[2]), [
                         "ERROR: INDIVIDUAL: US03: I4 on line: 44: Death date occurs before their date of birth."])
        inputGed1.close()

    def testUS32(self):
        inputGed = open("data/Sprint1.ged", "r")
        inputGed1 = open("data/input_8.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us32.checkMultipleBirths(output[2]), us32res)
        self.assertEqual(us32.checkMultipleBirths(output1[2]), us32res1)

    def testUS07(self):
        inputGed = open("data/Sprint1.ged", "r")
        inputGed1 = open("data/input_8.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us07.checkForLessThan150(output[0], output[2]), [
                         "ERROR: INDIVIDUAL: US07: I3 is older than 150 line 35"])
        self.assertEqual(us07.checkForLessThan150(output1[0], output1[2]), [
                         "ERROR: INDIVIDUAL: US07: I9 death - birth > 150 line 95"])

    def testUS29(self):
        inputGed = open("data/inputRZ1.ged", "r")
        inputGed1 = open("data/inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us29.deaths(output[0], output[2]), deaths1)
        self.assertEqual(us29.deaths(output1[0], output1[2]), deaths2)

    def testUS16(self):  # us16
        inputGed = open("data/inputRZ1.ged", "r")
        inputGed1 = open("data/inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us16.sameLastName(output[0], output[2]), name1)
        self.assertEqual(us16.sameLastName(output1[0], output1[2]), name2)

    def testUS06(self):
        inputGed = open("data/Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us06.main(output[0], output[1], output[3]), [
                         "ERROR: INDIVIDUAL: US06: I4: Divorce date occurs after their date of death on line 88"])

    def testUS04(self):
        inputGed = open("data/Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us04.marriageBeforeDivorce(output[1]), [
                         'ERROR: FAMILY: US04: F1: Divorce date occurs before their marriage.'])
        inputGed.close()

    def testUS05(self):
        inputGed = open("data/Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us05.main(output[0], output[1], output[3]), [
                         "ERROR: INDIVIDUAL: US05: I4: Marriage date occurs after their date of death on line 82."])
        inputGed.close()

    def testUS01(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        for i in individual:
            self.assertTrue(us01.BirthBeforeCurrent(i))
            self.assertTrue(us01.DeathBeforeCurrent(i))
            self.assertTrue(us01.MarriageBeforeCurrent(i))
            self.assertTrue(us01.DivorceBeforeCurrent(i))

    def testUS02(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        for indi in individual:
            self.assertTrue(us02.BirthBeforeMarriage(individual[indi]))

    def testUS35(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        self.assertEqual(us35.RecentBirths(individual), ['I1'])

    def testUS21(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for i in family:
            self.assertTrue(us21.CheckGenderForRole(
                family[i], individual))

    def testUS31(self):
        inputGed = open("data/Sprint1.ged", "r")
        inputGed1 = open("data/input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us31.checkForLivingSingle(output1[0], output1[2]), [
                         'ERROR: INDIVIDUAL: US31: I4 Rocky /Quinto/ on line: 45 is living and single', 'ERROR: INDIVIDUAL: US31: I11 John /Quinto/ on line: 117 is living and single'])
        inputGed.close()
        self.assertEqual(us31.checkForLivingSingle(output[0], output[2]), [])
        inputGed1.close()

    def testUS10(self):
        inputGed = open("data/Orphan.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us10.main(output[0], output[1], output[3]), ['ERROR: INDIVIDUAL: US10: I1 marriage date occurs before they are 15 on line 245', 'ERROR: INDIVIDUAL: US10: I4 marriage date occurs before they are 15 on line 260',
                                                                      'ERROR: INDIVIDUAL: US10: I5 marriage date occurs before they are 15 on line 245', 'ERROR: INDIVIDUAL: US10: I6 marriage date occurs before they are 15 on line 260'])

    def testUS14(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us14.main(output[0], output[1], output[3]), [
                         "ERROR: FAMILY: US14: F4 more than 5 siblings have multiple birthdays on year 2018 line 261"])

    def testUS22(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us22.uniqueIDs(output), (['I21'], []))

    def testUS26(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us26.corrEntries(output), ["ERROR: FAMILY: US26: Family F2 does not have the correct corresponding entries on line 231",
                                                    "ERROR: FAMILY: US26: Family F3 does not have the correct corresponding entries on line 237", "ERROR: FAMILY: US26: Family F4 does not have the correct corresponding entries on line 261"])

    def testUS15(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us15.checkFewerThan15(output[1], output[2]), [
                         "ERROR: FAMILY: US15: True I3 family has more than 15 siblings line 35"])

    def testUS18(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us18.main(output), [
                         "ERROR: FAMILY: US18: ['I8', 'I7'] Siblings should not marry on line 237."])

    def testUS30(self):
        inputGed = open("data/Sprint1.ged", "r")
        inputGed1 = open("data/input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        inputGed.close()
        self.assertEqual(us30.checkForLivingMarried(output), ['NOTE: INDIVIDUAL: US30: I1 Edward /Rogers/ is living and married on line 14', 'NOTE: INDIVIDUAL: US30: I3 Emily /Rogers/ is living and married on line 35',
                                                              'NOTE: INDIVIDUAL: US30: I5 Marcia /Rogers/ is living and married on line 56', 'NOTE: INDIVIDUAL: US30: I6 Tim /Jones/ is living and married on line 65'])

        self.assertEqual(us30.checkForLivingMarried(output1), ['NOTE: INDIVIDUAL: US30: I1 Chloe /Quinto/ is living and married on line 15', 'NOTE: INDIVIDUAL: US30: I2 Rafael /Quinto/ is living and married on line 25',
                                                               'NOTE: INDIVIDUAL: US30: I3 Maria /Quinto/ is living and married on line 35', 'NOTE: INDIVIDUAL: US30: I5 Thompson /L/ is living and married on line 54', 'NOTE: INDIVIDUAL: US30: I8 Grandpa /Loresco/ is living and married on line 86'])
        inputGed1.close()

    def testUS42(self):
        inputGed = open("data/inputRZ1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertTrue(us42.filterDates(output))

    def testUS33(self):
        inputGed = open("data/Orphan.ged", "r")
        output = readGed.fam(inputGed)
        self.assertTrue(us33.checkForOrphan(output[0], output[1], output[2]), [
                        "NOTE: US33: Individual I24 is an orphan on line 236"])

    def testUS41(self):
        self.assertEqual(
            us41.main(), "NOTE: US41: DATES ARE FIXED TO INCLUDE PARTIALS")

    def testUS40(self):
        self.assertEqual(us40.main(), "NOTE: US40: LINE NUMBERS ARE ADDED")

    def testUS08(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for index in family:
            for child in family[index].children:
                self.assertTrue(us08.BirthBeforeMarriageOfParents(
                    family[index], individual[child]))

    def testUS09(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for index in family:
            for child in family[index].children:
                self.assertTrue(us09.BirthBeforeDeathOfParents(
                    family[index], individual[child], individual))

    def testUS28(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us28.orderSiblings(output), {'F1': [['I1', -13, 14]], 'F2': [['I4', -19, 44]], 'F4': [['I7', 4, 74], ['I8', 3, 84]], 'F5': [['I10', 2, 104], ['I9', 0, 94]], 'F3': [
                         ['I11', 1, 114], ['I12', 1, 123], ['I13', 1, 132], ['I14', 1, 141], ['I15', 1, 150], ['I16', 1, 159], ['I17', 0, 168], ['I18', -1, 177], ['I19', -2, 186], ['I20', -3, 195], ['I21', -5, 213]]})

    def testUS36(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us36.main(output), None)

    def testUS38(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us38.main(output[0], output[2]), None)
        inputGed.close()

    def testUS39(self):
        inputGed = open("data/Sprint2.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us39.main(output[1], output[3]), None)
        inputGed.close()

    def testUS12(self):
        inputGed = open("data/Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us12.checkForOldParents(output[0], output[1], output[2]), ["ERROR: US12: Individual: I1's father is too old on line: 14",
                                                                                    "ERROR: US12: Individual: I1's mother is too old on line: 14", "ERROR: US12: Individual: I4's father is too old on line: 44", "ERROR: US12: Individual: I4's mother is too old on line: 44"])

    def testUS23(self):
        inputGed = open("data/UniqueNames.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us23.uniqueNameAndBirthday(output[0], output[2]), [
                         'ERROR: INDIVIDUAL: US23: I25 does not have a unique name and birthday on line: 245', 'ERROR: INDIVIDUAL: US23: I26 does not have a unique name and birthday on line: 254'])

    def testUS27(self):
        inputGed = open("data/Sprint3.ged")
        output = readGed.fam(inputGed)
        self.assertEqual(us27.listPeopleAndAge(output[0], output[2]), None)

    def testUS25(self):
        inputGed = open("data/Sprint3.ged")
        output = readGed.fam(inputGed)
        self.assertTrue(us25.uniqueFirstNames(output))

    def testUS34(self):
        inputGed = open("data/Sprint3.ged")
        output = readGed.fam(inputGed)
        self.assertEqual(us34.largeAgeDifferences(output[0], output[1], output[2]), ['ERROR: INDIVIDUAL: US34: Individual I5 was over twice as old as spouse I1 at their time of marriage on line: ',
                                                                                     'ERROR: INDIVIDUAL: US34: Individual I6 was over twice as old as spouse I4 at their time of marriage on line: '])

    def testUS13(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for i in family:
            temp = us13.SiblingsSpacing(family[i], individual)
            self.assertTrue(temp[0])

    def testUS24(self):
        inputGed = open("data/Sprint4.ged")
        allLists = readGed.fam(inputGed)
        # no clue why this is not returning errors
        self.assertEqual(us24.main(allLists[1], allLists[3]), ['ERROR: FAMILY: US24: DUPLICATE FAMILY: F11 WITH HUSBAND: Dan /Jones/ AND WIFE Ashley /Jones/ MARRIED ON 2035-04-30 on line 404'])

    def testUS20(self):
        inputGed = open("data/inputForTest_MW.ged", "r")
        result = us01.parseGed(inputGed)
        individual = result[0]
        family = result[1]
        for i in family:
            temp = us20.NotMarryNiecesAndNephews(family[i], family, individual)
            self.assertTrue(temp[0])
    
    def testUS37(self):
        inputGed = open("data/Sprint2.ged", "r")
        allLists = readGed.fam(inputGed)
        self.assertEqual(us37.main(allLists[0], allLists[1], allLists[3]), ["ERROR: FAMILY: US37: I2: passed within the last 30 days leaving behind their spouse: I3 and children: ['I1', 'I4'] on line 231"])
        inputGed.close()

    def testUS17(self): 
        inputGed = open("data/Sprint4.ged", "r")
        allLists = readGed.fam(inputGed)
        self.assertEqual(us17.main(allLists[1], allLists[3]), ['ERROR: FAMILY: US17: HUSBAND MARRIED HIS CHILD ON LINE: 410'])


if __name__ == '__main__':
    unittest.main()
