from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    #helper functions
    def check_for_row_in_list_table(self,row_text,elementId):
        table=self.browser.find_element_by_id(elementId)
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    
    #test functions
    def test_startAndRetrieveList(self):

        #Want to access app
        self.browser.get('http://127.0.0.1:8000/cv')

        #has "Arnaud Meriguet" in the titel and header
        self.assertIn ('Arnaud Meriguet', self.browser.title)

        #has 'CV' in the h2 tag
        cv_h2_text=self.browser.find_element_by_id('CVh2').text
        self.assertEqual('My CV',cv_h2_text)

        #The user is invited to add a skill to the list
        inputbox=self.browser.find_element_by_id('idNewSkill')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a skill')

        #in the CV page, the user enters a skill
        #types "Python" into a textbox
        inputbox.send_keys('Python')

        #hits Enter, page updates, page has now a skill named "Python"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_row_in_list_table('Python','idListSkills')
        #the box is still here waiting for more imputs
        #User inputs "Funtional testing"
        inputbox=self.browser.find_element_by_id('idNewSkill')
        inputbox.send_keys('Functional testing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        #page updates, both "python" and "Functional testing" can be seen on the CV
        self.check_for_row_in_list_table('Python','idListSkills')
        self.check_for_row_in_list_table('Functional testing','idListSkills')

        #A URL has been generated by the site. 
        #Clicks on it, the CV remembers the inputs
        self.fail('FINISH THE TEST!')

if __name__=='__main__':
    unittest.main(warnings='ignore')
