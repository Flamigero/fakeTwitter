""" FakeTwitter class tests """

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FakeTwitterPage(object):
    def __init__(self, os):
        if os == "windows":
            self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        else:
            self.driver = webdriver.Chrome(executable_path = './chromedriver')

        self.url = 'http://localhost:8000/users/login/'

    def open(self):
        """ Open web """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def login(self):
        """ Make login """
        email = self.driver.find_element_by_name('email')
        password = self.driver.find_element_by_name('password')
        #submit = self.driver.find_element_by_xpath('/html/body/section/form/input[4]')

        email.click()
        email.clear()
        email.send_keys('testing@testing.com')

        password.click()
        password.clear()
        password.send_keys('testing')
        password.submit()
