'''
All Unit Tests 
'''
import us03, us16, us29
import unittest
import readGed
from package.userStories import us07,us32

deaths1 = [
    ['I6', 'Grandpa /Quinto/', 'M', '1940-06-03', 64, 'False', '2004-07-17', 'NA', "{'F5'}", "{'F3'}", "{'F5'}"],
    ['I7', 'Grandma /Quinto/', 'F', '1940-06-11', 62, 'False', '2002-06-06', 'NA', "{'F3'}"],
    ['I9', 'Grandma /Loresco/', 'F', '1940-04-03', 54, 'False', '1994-10-16', 'NA', "{'F4'}"],
    ['I10', 'Ex /Quinto/', 'F', '1945-10-07', 56, 'False', '2001-07-13', 'NA', "{'F5'}"]
]

#Ex Quinto has age -144 or something

deaths2 = [
    ['I1', 'Bob /Smiath/', 'M', '1907-04-04', 92, 'False', '1999-10-31', "{'F2'}", "{'F1'}", "{'F1'}"],
    ['I2', 'Johnathan /Smith/', 'M', '1879-11-21', 80, 'False', '1959-04-10', 'NA', "{'F2'}"],
    ['I3', 'Dorothy /Rodgers/', 'F', '1879-10-01', 83, 'False', '1962-05-18', 'NA', "{'F2'}"],
    ['I4', 'Mary /Johnson/', 'F', '1908-02-03', 81, 'False', '1989-06-29', 'NA', "{'F1'}"],
    ['I6', 'Nancy /Jefferson/', 'F', '1942-02-15', 34, 'False', '1976-12-09', 'NA', "{'F4'}"]
]

name1 = (
    [['I2', 'Rafael /Quinto/', 'M', '1968-04-04', 51, 'True', 'NA', "{'F2'}", "{'F3'}", "{'F2'}"], ['I4', 'Rocky /Quinto/', 'M', '1995-06-28', 24, 'True', 'NA', "{'F2'}", 'NA'], ['I5', 'Thompson /L/', 'M', '1997-01-30', 22, 'True', 'NA', 'NA', "{'F1'}"], ['I6', 'Grandpa /Quinto/', 'M', '1940-06-03', 64, 'False', '2004-07-17', 'NA', "{'F5'}", "{'F3'}", "{'F5'}"], ['I8', 'Grandpa /Loresco/', 'M', '1940-10-05', 79, 'True', 'NA', 'NA', "{'F4'}"], ['I11', 'John /Quinto/', 'M', '1960-09-08', 59, 'True', 'NA', "{'F5'}", 'NA']],
    []
)

name2 = (
    [['I1', 'Bob /Smiath/', 'M', '1907-04-04', 92, 'False', '1999-10-31', "{'F2'}", "{'F1'}", "{'F1'}"], ['I2', 'Johnathan /Smith/', 'M', '1879-11-21', 80, 'False', '1959-04-10', 'NA', "{'F2'}"], ['I8', 'Michael /Smith/', 'M', '1975-03-20', 44, 'True', 'NA', "{'F4'}", 'NA']],
    ["ERROR US16: Brian /Smith/ does not have the same last name\n"]
)

class TestResults(unittest.TestCase): 
    def testbirthBeforeDeath(self):
        inputGed = open("input.ged", "r")
        inputGed1 = open("input_1.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        inputGed6 = open("input_6.ged", "r")
        output = readGed.fam(inputGed)
        
        self.assertEqual(us03.birthBeforeDeath(inputGed6), [['Ex /Quinto/', '1945-10-07', '1801-07-13']])
        inputGed.close()
        self.assertEqual(us03.birthBeforeDeath(inputGed1), [['Johnathan /Smith/', '1879-11-21', '1859-04-10']])
        inputGed1.close()
        inputGed2 = open("input_2.ged", "r")
        self.assertEqual(us03.birthBeforeDeath(inputGed2), [['Grandpa /Quinto/', '1940-06-03', '1804-07-17']])
        inputGed2.close()
        self.assertEqual(us03.birthBeforeDeath(inputGed3), [['Grandma /Loresco/', '1940-04-03', '1894-10-16']])
        inputGed3.close()
        self.assertEqual(us03.birthBeforeDeath(inputGed4), [['Grandma /Quinto/', '1940-06-11', '1902-06-06']])
        inputGed4.close()
    
    def testMultipleBirths(self): #US32
        inputGed = open("input.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        self.assertEqual(us32.checkMultipleBirths(""), [])
        self.assertEqual(us32.checkMultipleBirths(inputGed), "No multiple births found")
        self.assertEqual(us32.checkMultipleBirths(inputGed2), "Family F2 experienced multiple birth dates on 12/27/1997")
        self.assertEqual(us32.checkMultipleBirths(inputGed3), "Family F2 experienced multiple birth dates on 09/09/1968")
        self.assertEqual(us32.checkMultipleBirths(inputGed4), "Family ['F2'] experienced multiple birth dates on ['12/27/1997', '09/09/1968']")


    def testLessThan150(self): #US07 
        inputGed7 = open("input_7.ged", "r")
        inputGed8 = open("input_8.ged", "r")
        self.assertEqual(us07.checkForLessThan150(""), [])
        self.assertTrue(us07.checkForLessThan150(inputGed7))
        self.assertFalse(us07.checkForLessThan150(inputGed8))



    def testDeaths(self):
        inputGed = open("inputRZ1.ged", "r")
        inputGed1 = open("inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us29.deaths(output[0]), deaths1)
        self.assertEqual(us29.deaths(output1[0]), deaths2)

    def testNames(self):
        inputGed = open("inputRZ1.ged", "r")
        inputGed1 = open("inputRZ2.ged", "r")
        output = readGed.fam(inputGed)
        output1 = readGed.fam(inputGed1)
        self.assertEqual(us16.sameLastName(output[0]), name1)
        self.assertEqual(us16.sameLastName(output1[0]), name2)
    

if __name__ == '__main__':   
    unittest.main() 
    