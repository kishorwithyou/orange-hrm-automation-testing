from selenium.webdriver.common.by import By

PROFILE_BUTTON = (By.XPATH, "//a[@id='welcome']")   

LOGOUT_BUTTON = (By.XPATH, "//a[@href='/index.php/auth/logout']")   

MYINFO_BUTTON = (By.ID, "My Info")     

PERSONAL_DETAILS = (By.XPATH, "//a[@href='/index.php/pim/viewPersonalDetails/empNumber/7']")   

EDIT_BUTTON = (By.XPATH, "//input[@id='btnSave']")    

SAVE_BUTTON = (By.ID, "btnSave")  

CONTACT_DETAIL_PAGE = (By.XPATH, "//h1[text()='Contact Details']")   

CONTACT_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/contactDetails/empNumber/7']")    

CHANGE_PHOTO = (By.XPATH, "//img[@id='empPic']")   

PHOTOGRAPH_PAGE = (By.XPATH, "//h1[text()='Photograph']")  

EMERGENCY_CONTACT = (By.XPATH, "//a[@href='/index.php/pim/viewEmergencyContacts/empNumber/7']")   

ASSIGNED_EMERGENCY_CONTACTS = (By.XPATH, "//h1[text()='Assigned Emergency Contacts']") 

DEPENDENT_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewDependents/empNumber/7']") 

ASSIGNED_DEPENDENTS = (By.XPATH, "//h1[text()='Assigned Dependents']") 
   
IMMEGRATION_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewImmigration/empNumber/7']")   

ASSIGNED_IMMEGRATION_RECORD = (By.XPATH, "//h1[text()='Assigned Immigration Records']") 

JOB_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewJobDetails/empNumber/7']")   

JOB_DETAIL_PAGE = (By.XPATH, "//h1[text()='Job']")

SALARY_BUTTON =  (By.XPATH, "//a[@href='/index.php/pim/viewSalaryList/empNumber/7']") 

ASSIGNED_SALARY_COMPONENT_PAGE = (By.XPATH, "//h1[text()='Assigned Salary Components']")

TAX_EXEMPTION_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewUsTaxExemptions/empNumber/7']")  

TAX_EXEMPTION_PAGE = (By.XPATH, "//h1[text()='Tax Exemptions']") 

REPORT_TO_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewReportToDetails/empNumber/7']") 

ASSIGNED_SUPERVISORS_SECTION = (By.XPATH, "//h1[text()='Assigned Supervisors']")  

ASSIGNED_SUBORDINATE_SECTION = (By.XPATH, "//h1[text()='Assigned Subordinates']")

QUALIFICATION_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewQualifications/empNumber/7']") 

WORK_EXPERIENCE = (By.XPATH, "//h1[text()='Work Experience']")  

EDUCATION = (By.XPATH, "//h1[text()='Education']")  

SKILLS = (By.XPATH, "//h1[text()='Skills']")   

LANGUAGES = (By.XPATH, "//h1[text()='Languages']")  

LICENSES = (By.XPATH, "//h1[text()='License']") 

MEMBERSHIP_BUTTON = (By.XPATH, "//a[@href='/index.php/pim/viewMemberships/empNumber/7']")  

ASSIGNED_MEMBERSHIP_PAGE = (By.XPATH, "//h1[text()='Assigned Memberships']")
