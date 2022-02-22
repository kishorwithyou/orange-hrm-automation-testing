from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "txtUsername")     #this line means we want to find a element whose NAME is q
PASSWORD_INPUT = (By.ID, "txtPassword")     #this line means we want to find a element whose NAME is q
LOGIN_BUTTON = (By.ID, "btnLogin")     #this line means we want to find a element whose NAME is q
MYINFO_BUTTON = (By.ID, "menu_pim_viewMyDetails")     #this line means we want to find a element whose NAME is q
INVALID_CRREDANTIAL = (By.XPATH, "//span[@id='spanMessage']")     #this line means we want to find a element whose NAME is q
    