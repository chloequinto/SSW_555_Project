'''
Chloe Quinto 
Unit Tests 

For User Story 32 List Multiple Births 

'''
import us29
import us32
import unittest

class TestResults(unittest.TestCase): 
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


    ### here add your tests 
    def testDeaths(self):
        inputGed = open("input.ged", "r")
        inputGed1 = open("input_1.ged", "r")
        inputGed2 = open("input_2.ged", "r")
        inputGed3 = open("input_3.ged", "r")
        inputGed4 = open("input_4.ged", "r")
        self.assertEqual(us29.deaths(inputGed), True)
        self.assertEqual(us29.deaths(inputGed1), [['/Smith/', '/Smith/'], ['/Smith/']])
        self.assertEqual(us29.deaths(inputGed2), False)
        self.assertEqual(us29.deaths(inputGed3), False)
        self.assertEqual(us29.deaths(inputGed4), True)

if __name__ == '__main__':   
    unittest.main() 
    