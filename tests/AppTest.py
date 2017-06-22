'''
Created on Jun 21, 2017

@author: Shrikanth
'''

from TestBase import TestBase
import unittest
from HomeScreen import HomeScreen

class AndroidTests(TestBase):
    #Any method name which starts with is prepended with test is considered as testcase
    def test_progress_to_subsection(self):
        homeScreen = HomeScreen(self)
        homeScreen.enterSection("App")
        homeScreen.goBackToHomeScreen();
        
    def test_homescreen_elements(self):
        homeScreen = HomeScreen(self)
        homeScreen.verifyListElements()

if __name__ == '__main__':
    #Creation of suite can be done by any framework. In this case main function is used to create a testsuite.
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)