'''
All Unit Tests 
'''
import us29
import us32
import us03_test
import unittest
import readGed

class TestResults(unittest.TestCase): 
    def testbirthBeforeDeath(self):
        inputGed = open("input.ged", "r")
        inputGed1 = open("input_1.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        output = readGed.fam(inputGed)
        
        self.assertEqual(us03_test.birthBeforeDeath(inputGed), [['Ex /Quinto/', '1945-10-07', '1801-07-13']])
        inputGed.close()
        self.assertEqual(us03_test.birthBeforeDeath(inputGed1), [['Johnathan /Smith/', '1879-11-21', '1859-04-10']])
        inputGed1.close()
        inputGed2 = open("input_2.ged", "r")
        self.assertEqual(us03_test.birthBeforeDeath(inputGed2), [['Grandpa /Quinto/', '1940-06-03', '1804-07-17']])
        inputGed2.close()
        self.assertEqual(us03_test.birthBeforeDeath(inputGed3), [['Grandma /Loresco/', '1940-04-03', '1894-10-16']])
        inputGed3.close()
        self.assertEqual(us03_test.birthBeforeDeath(inputGed4), [['Grandma /Quinto/', '1940-06-11', '1902-06-06']])
        inputGed4.close()
    
    def test_multipleBirths(self): 
        inputGed = open("input.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        self.assertEqual(us32.checkMultipleBirths(""), [])
        self.assertEqual(us32.checkMultipleBirths(inputGed), "No multiple births found")
        self.assertEqual(us32.checkMultipleBirths(inputGed2), "Family F2 experienced multiple birth dates on 12/27/1997")
        self.assertEqual(us32.checkMultipleBirths(inputGed3), "Family F2 experienced multiple birth dates on 09/09/1968")
        self.assertEqual(us32.checkMultipleBirths(inputGed4), "Family ['F2'] experienced multiple birth dates on ['12/27/1997', '09/09/1968']")

    def testDeaths(self):
        inputGed = open("input.ged", "r")
        inputGed1 = open("input_1.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        output = readGed.fam(inputGed)
        self.assertEqual(us29.deaths(output), True)
        self.assertEqual(us29.deaths(inputGed1), [['/Smith/', '/Smith/'], ['/Smith/']])
        self.assertEqual(us29.deaths(inputGed2), False)
        self.assertEqual(us29.deaths(inputGed3), False)
        self.assertEqual(us29.deaths(inputGed4), True)
    
    

if __name__ == '__main__':   
    unittest.main() 
    