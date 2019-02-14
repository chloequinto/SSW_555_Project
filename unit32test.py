'''
Chloe Quinto 
Unit Tests 

For User Story 32 List Multiple Births 

'''
import us32
import unittest 

class TestResults(unittest.TestCase): 
    def test_multipleBirths(self): 
        inputGed = open("input.ged", "r")
        inputGed1 = open("input_us32.ged", "r")
        inputGed2 = open("input_us32_2.ged", "r")
        self.assertEqual(us32.checkMultipleBirths(""), [])
        self.assertEqual(us32.checkMultipleBirths(inputGed), "No multiple births found")
        self.assertEqual(us32.checkMultipleBirths(inputGed1), "Fam: experienced multiple birth dates on 27 DEC 1997")
        self.assertEqual(us32.checkMultipleBirths(inputGed2), "Fam: experienced multiple birth dates on ")
        # self.assertEqual(us32.checkMultipleBirths(inputGed2), "Fam: experienced multiple birth dates on 27 DEC 1997\nFam: experienced multiple birth dates on 9 SEP 1968")


    ### here add your tests 

if __name__ == '__main__':   
    unittest.main() 
    