from selenium.webdriver.common.by import By

from locator.login_page_locator import MYINFO_BUTTON

PROFILE_BUTTON = (By.XPATH, "//a[@id='welcome']")     #this line means we want to find a element whose NAME is q
LOGOUT_BUTTON = (By.XPATH, "//a[@href='/index.php/auth/logout']")     #this line means we want to find a element whose NAME is q
MYINFO_BUTTON = (By.ID, "My Info")     #this line means we want to find a element whose NAME is q
PERSONAL_DETAILS = (By.XPATH, "//a[@href='/index.php/pim/viewPersonalDetails/empNumber/7']")     #this line means we want to find a element whose NAME is q
