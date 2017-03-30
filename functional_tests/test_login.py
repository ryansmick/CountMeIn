from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest
from django.contrib.auth.models import User

class LoginTest(FunctionalTest):
    
    def test_can_create_account(self):
        User.objects.create_user('test@test.com', 'test@test.com', 'samplepassword') # ONLY USE TEMPORARILY! CREATE SIGNUP ABILITY FOR USER!
        
        # A new user goes to the site and sees a header bar with a signup button
        self.browser.get(self.live_server_url)
        self.fail("Not yet implemented!")
        
        # The user clicks the signup button and creates an account
        
        # The user clicks the submit button and is logged into his account when the page reloads, which he can tell from the new navbar
        
        # The user then logs out of his account by clicking the logout button in the navbar
        
    def test_can_login(self):
        User.objects.create_user('test@test.com', 'test@test.com', 'samplepassword') # ONLY USE TEMPORARILY! CREATE SIGNUP ABILITY FOR USER!
        
        # A new user goes to the site and sees a header bar with a signup button
        self.browser.get(self.live_server_url)
        
        # The user then decides he wants to log in, so he clicks the login button
        self.browser.find_element_by_id("loginModalLink").click()
        
        # The user waits for the login modal to pop up
        self.wait_for(
            lambda: self.browser.find_element_by_id('loginEmail')
        )
        
        # He enters incorrect info at first, and is treated with an error message
        self.login("test@test.com", "incorrectpassword")
        
        self.wait_for(
            lambda: self.browser.find_element_by_id("loginAlert")
        )
        
        self.assertIn("Invalid", self.browser.find_element_by_id("loginAlert").text)
        
        #He then enters the right info
        self.login("test@test.com", "samplepassword")
        
        # The user waits for the page to reload
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Logout')
        )
        
        # The user is now logged back in, and is shown the new navbar
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn("Groups", navbar.text)
        
    # Function to ease login process
    def login(self, email, password):
        emailBox = self.browser.find_element_by_id("loginEmail")
        passBox = self.browser.find_element_by_id("loginPassword")
        # The user enteres his information into the login modal
        emailBox.clear()
        emailBox.send_keys(email)
        passBox.clear()
        passBox.send_keys(password)
        
        # The user then clicks the submit button, and waits for the page to reload
        self.browser.find_element_by_id("loginSubmit").click()
        
        
