import unittest
import tax

class CalculatorTestCase(unittest.TestCase):

    def test_1people0(self):
        
        result = tax.Cal1people(132000,0)
        self.assertEqual(result, 0)
        
    def test_1people(self):
        
        result = tax.Cal1people(500000,18000)
        self.assertEqual(result, 41500)
    
    def test_1people2(self):
        
        result = tax.Cal1people(800000,18000)
        self.assertEqual(result, 92500)

    def test_1people3(self):
        
        result = tax.Cal1people(2040050,18000)
        self.assertEqual(result, 303307)
        
    def test_2people(self):
        
        result = tax.Cal2peopleSelfnSpouse(600000,400000,18000,18000)
        self.assertEqual(result, 83000)
    
    def test_2people2(self):
        
        result = tax.Cal2peopleSelfnSpouse(1000000,1000000,18000,18000)
        self.assertEqual(result, 253000)
        
    def test_2people3(self):
        
        result = tax.Cal2peopleSelfnSpouse(2000000,1000000,18000,18000)
        self.assertEqual(result, 423000)
        
    def test_2people4(self):  
        
        result = tax.Cal2peopleSelfnSpouse(2040050,2040050,18000,18000)
        self.assertEqual(result, 606614)
    
    def test_2peopletotal(self):
        
        result = tax.Cal2peopletotal(600000,400000,18000,18000)
        self.assertEqual(result, 101000)
    
    def test_2peopletotal2(self):
        
        result = tax.Cal2peopletotal(1000000,1000000,18000,18000)
        self.assertEqual(result, 271000)
    
    def test_2peopletotal3(self):
        
        result = tax.Cal2peopletotal(2040050,2040050,18000,18000)
        self.assertEqual(result, 606615)
    
    def test_2peopletotal4(self): #Fail answer#
        
        result = tax.Cal2peopletotal(2040050,2040050,18000,18000)
        self.assertEqual(result, 99999)
    
    
    def test_checkfunction(self):
        
        result = tax.Checknum(83000,101000)
        self.assertEqual(result, "Suggest using Separate Taxation which are lower tax")
        
        
    def test_checkfunction2(self):
    
        result = tax.Checknum(423000,441000)
        self.assertEqual(result, "Suggest using Separate Taxation which are lower tax")    


if __name__ == '__main__':
    unittest.main()
