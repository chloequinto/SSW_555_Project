'''
All Unit Tests 
'''
import us03, us16, us29, us06, us04, us05, us22, us15, us26, us35, us01, us02, us21, us31, us10
import unittest
import readGed
from package.userStories import us07,us32

deaths1 = [
    ['I6', 'Grandpa /Quinto/', 'M', '1940-06-03', 64, 'False', '2004-07-17', 'NA', "{'F5'}", "{'F3'}", "{'F5'}"],
    ['I7', 'Grandma /Quinto/', 'F', '1940-06-11', 62, 'False', '2002-06-06', 'NA', "{'F3'}"],
    ['I9', 'Grandma /Loresco/', 'F', '1940-04-03', 54, 'False', '1994-10-16', 'NA', "{'F4'}"],
    ['I10', 'Ex /Quinto/', 'F', '1945-10-07', 56, 'False', '2001-07-13', 'NA', "{'F5'}"]
]

deaths2 = [
    ['I1', 'Bob /Smiath/', 'M', '1907-04-04', 92, 'False', '1999-10-31', "{'F2'}", "{'F1'}", "{'F1'}"],
    ['I1', 'Johnathan /Smith/', 'M', '1879-11-21', 80, 'False', '1959-04-10', 'NA', "{'F2'}"],
    ['I3', 'Dorothy /Rodgers/', 'F', '1879-10-01', 83, 'False', '1962-05-18', 'NA', "{'F2'}"],
    ['I4', 'Mary /Johnson/', 'F', '1908-02-03', 81, 'False', '1989-06-29', 'NA', "{'F1'}"],
    ['I6', 'Nancy /Jefferson/', 'F', '1942-02-15', 34, 'False', '1976-12-09', 'NA', "{'F4'}"]
]

name1 = (
    [
        ['I2', 'Rafael /Quinto/', 'M', '1968-04-04', 51, 'True', 'NA', "{'F2'}", "{'F3'}", "{'F2'}"], 
        ['I4', 'Rocky /Quinto/', 'M', '1995-06-28', 24, 'True', 'NA', "{'F2'}", 'NA'], 
        ['I5', 'Thompson /L/', 'M', '1997-01-30', 22, 'True', 'NA', 'NA', "{'F1'}"],
        ['I6', 'Grandpa /Quinto/', 'M', '1940-06-03', 64, 'False', '2004-07-17', 'NA', "{'F5'}", "{'F3'}", "{'F5'}"], 
        ['I8', 'Grandpa /Loresco/', 'M', '1940-10-05', 79, 'True', 'NA', 'NA', "{'F4'}"], 
        ['I11', 'John /Quinto/', 'M', '1960-09-08', 59, 'True', 'NA', "{'F5'}", 'NA']
    ],
    []
)

name2 = (
    [
        ['I1', 'Johnathan /Smith/', 'M', '1879-11-21', 80, 'False', '1959-04-10', 'NA', "{'F2'}"], 
        ['I8', 'Michael /Smith/', 'M', '1975-03-20', 44, 'True', 'NA', "{'F4'}", 'NA'],
    ],
    [
        "ERROR: INDIVIDUAL: US16: Bob /Smiath/ does not have the same last name",
        "ERROR: INDIVIDUAL: US16: Brian /Smith/ does not have the same last name"
    ]
)

us07res = (
    ["ERROR: INDIVIDUAL: US32: I1 has the same birthdays as someone else on ['2032-06-10']",
    "ERROR: INDIVIDUAL: US32: I4 has the same birthdays as someone else on ['2032-06-10']"]
)

us07res1 = (
    ["ERROR: INDIVIDUAL: US32: I3 has the same birthdays as someone else on ['1995-06-28']",
    "ERROR: INDIVIDUAL: US32: I4 has the same birthdays as someone else on ['1995-06-28']"]
)

class TestResults(unittest.TestCase): 

    maxDiff = None #check for full errors
    
    def testbirthBeforeDeath(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us03.birthBeforeDeath(output1[0]), ["ERROR: INDIVIDUAL: US03: I10 has a death date before their date of birth."])
        inputGed.close()
        self.assertEqual(us03.birthBeforeDeath(output[0]), ["ERROR: INDIVIDUAL: US03: I4 has a death date before their date of birth."])
        inputGed1.close()
    
    def testUS32(self): #US32
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_8.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us32.checkMultipleBirths(output[0]),us07res)
        self.assertEqual(us32.checkMultipleBirths(output1[0]),us07res1)

    def testUS07(self): #US07 
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_8.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us07.checkForLessThan150(output[0]), ["ERROR: INDIVIDUAL: US07: I3 is older than 150"])
        self.assertEqual(us07.checkForLessThan150(output1[0]), ["ERROR: INDIVIDUAL: US07: I9 death - birth > 150"])

    def testDeaths(self):
        inputGed = open("inputRZ1.ged", "r")
        inputGed1 = open("inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us29.deaths(output[0]), deaths1)
        self.assertEqual(us29.deaths(output1[0]), deaths2) 

    def testNames(self): #us16
        inputGed = open("inputRZ1.ged", "r")
        inputGed1 = open("inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us16.sameLastName(output[0]), name1)
        self.assertEqual(us16.sameLastName(output1[0]), name2)

    def testUS06(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us06.main(output[0], output[1]), ["ERROR: INDIVIDUAL: US06: I4: Divorce date occurs after their date of death."])

    def testmarriageBeforeDivorce(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us04.marriageBeforeDivorce(output[1]), ['ERROR: FAMILY: US04: F1: Divorce date occurs before their marriage.'])
        inputGed.close()
        
    def testmarriageBeforeDeath(self):
        inputGed = open("Sprint1.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us05.main(output[0], output[1]), ["ERROR: INDIVIDUAL: US05: I4: Marriage date occurs after their date of death."])
        inputGed.close()

    def test_dateBeforeCurrent(self):
        inputGed = open("inputForTest_MW.ged", "r")
        individual = us01.parseGed(inputGed)
        for i in individual:
            self.assertTrue(us01.BirthBeforeCurrent(i),msg="ERROR: INDIVIDUAL: US01: "+ individual[i].ID + ": Birthday " + individual[i].birthDate + " occurs in the future")
            self.assertTrue(us01.DeathBeforeCurrent(i),msg="ERROR: INDIVIDUAL: US01: "+ individual[i].ID + ": Death date " + individual[i].deathDate + " occurs in the future")
            self.assertTrue(us01.MarriageBeforeCurrent(i),msg="ERROR: INDIVIDUAL: US01: "+ individual[i].ID + ": Marriage date " + individual[i].marriageDate + " occurs in the future")
            self.assertTrue(us01.DivorceBeforeCurrent(i),msg="ERROR: INDIVIDUAL: US01: "+ individual[i].ID + ": Divorce date " + individual[i].divorceDate + " occurs in the future")
    
    
    def test_birthBeforeMarriage(self):
        inputGed = open("inputForTest_MW.ged", "r")
        individual = us02.parseGed(inputGed)
        for indi in individual:
            self.assertTrue(us02.BirthBeforeMarriage(individual[indi]),msg="ERROR: INDIVIDUAL: US02: "+ individual[indi].ID + ": Birthday " + individual[indi].birthDate + " occurs before marriage " + individual[indi].marriageDate)

    def testRecentBirth(self):
        inputGed = open("inputForTest_MW.ged", "r")
        individual = us35.parseGed(inputGed)
        self.assertEqual(us35.RecentBirths(individual),['I1'])

    def testGenderForRole(self):
        inputGed = open("inputForTest_MW.ged", "r")
        family = us21.parseGed(inputGed)
        for i in family:
            self.assertTrue(us21.CheckGenderForRole(
                i), msg="ERROR: FAMILY: US21: " + family[i].ID + ": gender was wrong")
    def testUS31(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us31.checkForLivingSingle(output1[0]), ['ERROR: INDIVIDUAL: US31 I4 Rocky /Quinto/ is living and single', 'ERROR: INDIVIDUAL: US31 I11 John /Quinto/ is living and single'])
        inputGed.close()
        self.assertEqual(us31.checkForLivingSingle(output[0]), [])
        inputGed1.close()

    def testUS10(self):
        inputGed = open("Sprint1.ged", "r")
        inputGed1 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us10.main(output[0], output[1]), ['ERROR: INDIVIDUAL: US10: I1 marriage date occurs before they are 15', 'ERROR: INDIVIDUAL: US10: I4 marriage date occurs before they are 15', 'ERROR: INDIVIDUAL: US10: I5 marriage date occurs before they are 15', 'ERROR: INDIVIDUAL: US10: I6 marriage date occurs before they are 15'])
        inputGed1.close()
        
       
        

    
if __name__ == '__main__':   


    unittest.main() 