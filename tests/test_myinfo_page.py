from locator.home_page_locator import MYINFO_BUTTON, PERSONAL_DETAILS
from locator.myinfo_page_locator import   ASSIGNED_DEPENDENTS, ASSIGNED_EMERGENCY_CONTACTS, ASSIGNED_IMMEGRATION_RECORD, ASSIGNED_MEMBERSHIP_PAGE, ASSIGNED_SALARY_COMPONENT_PAGE, ASSIGNED_SUBORDINATE_SECTION,ASSIGNED_SUPERVISORS_SECTION, CHANGE_PHOTO, CONTACT_BUTTON, CONTACT_DETAIL_PAGE, DEPENDENT_BUTTON, EDIT_BUTTON, EDUCATION, EMERGENCY_CONTACT, IMMEGRATION_BUTTON, JOB_BUTTON, JOB_DETAIL_PAGE, LANGUAGES, LICENSES, MEMBERSHIP_BUTTON, PHOTOGRAPH_PAGE, QUALIFICATION_BUTTON, REPORT_TO_BUTTON, SALARY_BUTTON, SAVE_BUTTON, SKILLS, TAX_EXEMPTION_BUTTON, TAX_EXEMPTION_PAGE, WORK_EXPERIENCE
from tests import BaseClass
from locator.login_page_locator import *

class TestLoginPage(BaseClass):
   def test_1_login(self):
        ''' This is a test case to test the login page or orange HRM.'''
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
   
   def test_2_myinfo(self):
        ''' This is a test case to display personal details to Ess user.'''
        #Instantiating the logger
        self.log().info("myinfo Orange HRM Test Started")
        #accessing the search field and sending jag to that
        self.get_element(MYINFO_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(PERSONAL_DETAILS).is_displayed()

   def test_3_personal_details(self):
        ''' This is a test case to edit personal details by Ess user.'''
        #Instantiating the logger
        self.log().info("personal details edit Orange HRM Test Started")
        #accessing the search field and sending jag to that
        self.get_element(EDIT_BUTTON).click()
        self.get_element(SAVE_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(PERSONAL_DETAILS).is_displayed()    

   def test_4_contact_details(self):
        ''' This is a test case to display contact details to Ess user. Ess user add contact details. Ess user can add multiple contact details'''
        #Instantiating the logger
        self.log().info("contact details test case Started")
        #accessing the search field and sending jag to that
        self.get_element(CONTACT_BUTTON).click()
        self.get_element(EDIT_BUTTON).click()
        self.get_element(SAVE_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(CONTACT_DETAIL_PAGE).is_displayed()     

   def test_5_add_photograph(self):
        ''' This is test case for ESS user can add a photograph.'''
        #Instantiating the logger
        self.log().info("Add Photograph Test Started")
        #accessing the search field and sending jag to that
        self.get_element(CHANGE_PHOTO).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(PHOTOGRAPH_PAGE).is_displayed()     

   def test_6_emergency_contact(self):
        ''' This is test case for ESS user can add a emergency contact. ESS user can add multiple emergency contact. ESS user can delete emergency contact'''
        #Instantiating the logger
        self.log().info("emergency contact Test Started")
        #accessing the search field and sending jag to that
        self.get_element(EMERGENCY_CONTACT).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(ASSIGNED_EMERGENCY_CONTACTS).is_displayed()   

   def test_7_dependents(self):
        ''' This is test case for ESS user view  dependent.'''
        #Instantiating the logger
        self.log().info("dependents Test Started")
        #accessing the search field and sending jag to that
        self.get_element(DEPENDENT_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(ASSIGNED_DEPENDENTS).is_displayed()   

   def test_8_immegration(self):
        ''' This is test case for ESS user can view/add immegration details.'''
        #Instantiating the logger
        self.log().info("immegration Test Started")
        #accessing the search field and sending jag to that
        self.get_element(IMMEGRATION_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(ASSIGNED_IMMEGRATION_RECORD).is_displayed()   

   def test_9_job_details(self):
        ''' This is test case for ESS user can view job details. ESS user restricted to edit job details.s'''
        #Instantiating the logger
        self.log().info("job details Test Started")
        #accessing the search field and sending jag to that
        self.get_element(JOB_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(JOB_DETAIL_PAGE).is_displayed()   

   def test_10_salary(self):
        ''' This is test case for ESS user can view salary details.'''
        #Instantiating the logger
        self.log().info("immegration Test Started")
        #accessing the search field and sending jag to that
        self.get_element(SALARY_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(ASSIGNED_SALARY_COMPONENT_PAGE).is_displayed()   

   def test_11_tax_exemption(self):
        ''' This is test case for ESS user can view tax exemption details by clicking tax exemption button.'''
        #Instantiating the logger
        self.log().info("immegration Test Started")
        #accessing the search field and sending jag to that
        self.get_element(TAX_EXEMPTION_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(TAX_EXEMPTION_PAGE).is_displayed()  
  
   def test_12_report_to(self):
        ''' This is test case for ESS user can view supervisiors details by clicking report-to button.'''
        #Instantiating the logger
        self.log().info("immegration Test Started")
        #accessing the search field and sending jag to that
        self.get_element(REPORT_TO_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(ASSIGNED_SUPERVISORS_SECTION).is_displayed() 
        assert self.get_element(ASSIGNED_SUBORDINATE_SECTION).is_displayed()     

   def test_13_qualification(self):
        ''' This is test case for ESS user can qualificatio details by clicking qualification button.'''
        #Instantiating the logger
        self.log().info("immegration Test Started")
        #accessing the search field and sending jag to that
        self.get_element(QUALIFICATION_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(WORK_EXPERIENCE).is_displayed()  
        assert self.get_element(EDUCATION).is_displayed()  
        assert self.get_element(SKILLS).is_displayed()    
        assert self.get_element(LANGUAGES).is_displayed() 
        assert self.get_element(LICENSES).is_displayed()     

   def test_14_membership(self):
        ''' This is test case for ESS user can view membership details by clicking tax memberhip button.'''
        #Instantiating the logger
        self.log().info("immegration Test Started")
        #accessing the search field and sending jag to that
        self.get_element(MEMBERSHIP_BUTTON).click()
        #logging the test success
        self.log().info("Test Success")
        # logout_page.get_logout_field().submit()
        assert self.get_element(ASSIGNED_MEMBERSHIP_PAGE).is_displayed()  