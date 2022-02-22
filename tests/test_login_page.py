from locator.home_page_locator import MYINFO_BUTTON
from tests import BaseClass
from locator.login_page_locator import *

class TestLoginPage(BaseClass): 
  def test_1_login(self):
        ''' This is a test case to test login with invalid user name and valid password.'''
        #Instantiating the logger
        self.log().info("login Orange HRM Test Started")
        #accessing the search field and sending jag to that
        self.get_element(USERNAME_INPUT).send_keys('User')
        self.get_element(PASSWORD_INPUT).send_keys('admin123')
        #accessing the submit button and clicking it
        self.get_element(LOGIN_BUTTON).submit()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(INVALID_CRREDANTIAL).is_displayed()
   
  def test_2_login(self):
        ''' This is a test case to test the login with valid user name and invlid password'''
        #Instantiating the logger
        self.log().info("login Orange HRM Test Started")
        #accessing the search field and sending jag to that
        self.get_element(USERNAME_INPUT).send_keys('Admin')
        self.get_element(PASSWORD_INPUT).send_keys('user123')
        #accessing the submit button and clicking it
        self.get_element(LOGIN_BUTTON).submit()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(INVALID_CRREDANTIAL).is_displayed()
   
  def test_3_login(self):
        ''' This is a test case to test the Orange HRM page of login with invalid username and invalid password.'''
        #Instantiating the logger
        self.log().info("login Orange HRM Test Started")
        #accessing the search field and sending jag to that
        self.get_element(USERNAME_INPUT).send_keys('User')
        self.get_element(PASSWORD_INPUT).send_keys('user123')
        #accessing the submit button and clicking it
        self.get_element(LOGIN_BUTTON).submit()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(INVALID_CRREDANTIAL).is_displayed()
   
  def test_4_login(self):
        ''' This is a test case to test the Orange HRM page of login.'''
        #Instantiating the logger
        self.log().info("login Orange HRM Test Started")
        #accessing the search field and sending jag to that
        self.get_element(USERNAME_INPUT).send_keys('Admin')
        self.get_element(PASSWORD_INPUT).send_keys('admin123')
        #accessing the submit button and clicking it
        self.get_element(LOGIN_BUTTON).submit()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(MYINFO_BUTTON).is_displayed()
   