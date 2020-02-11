from selenium import webdriver
from time import sleep

from secrets import phoneNumber

class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome()


    def goToBaseSite(self):
        try:
            self.driver.get('http://tinder.com')
            # 2 seconds for page load
            sleep(2)
        except Exception:
            print('Error accessing base url', Exception)
        


    def loginWithPhoneNumber(self):
        try:
            # select login option (phone number)
            phoneLogin = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
            phoneLogin.click()

            # 2 seconds for page load
            sleep(2)

            # enter phone number
            phone_input = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
            # enter phone number
            phone_input.send_keys(phoneNumber)

            # click continue
            continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            continue_btn.click()

            # get 2fa from user
            two_factor_code = int(input("Enter 2fa Code: "))

            # enter 2fa code
            two_factor_input = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[1]')
            two_factor_input.send_keys(two_factor_code)

            # click continue
            continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button');
            continue_btn.click()

        except Exception:
            print('error logining in with phone number', Exception)
        
       

    def handle_popups_after_login(self):
        try:
            # sleep for 2 seconds
            sleep(2)
            # handle popups
            # location services
            popup_1 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_1.click()

            # notifications
            popup_2 = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()
        except Exception:
            print('error dismissing popups after logging in', Exception)
        


    def login(self):
        self.goToBaseSite()
        self.loginWithPhoneNumber()
        
        self.handle_popups_after_login()

    
    def like(self):
        like_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

        
    def dislike(self):
        dislike_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_popup(self):
        # add tinder to home screen
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()