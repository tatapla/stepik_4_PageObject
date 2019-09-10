from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	LOGIN_EMAIL = (By.CSS_SELECTOR, "#login_form [type='email']")
	LOGIN_PASSWORD = (By.CSS_SELECTOR, "#login_form [type='password']")
	LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form [name='login_submit']")