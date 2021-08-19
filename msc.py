import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Essential():

    # Config Parameters
    url = 'https://toolscms-mobile.terra.com/MSC/adm/account/logon.aspx?ReturnUrl=%2fMSC%2fadm%2f'
    username = 'rafael.dmoreira'
    password = 'T3rra#2021!'
    filename = 'msisdn_list.txt'

    def set_config_run(self):

        chrome_options = Options()
        #''' Headless Option
        chrome_options.add_argument("headless")
        chrome_options.add_argument("no-sandbox")
        #'''
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.url)

        inputElement = driver.find_element_by_id("LoginUser_UserName")
        inputElement.send_keys(self.username)
        time.sleep(1)
        inputElement = driver.find_element_by_id("LoginUser_Password")
        inputElement.send_keys(self.password)
        time.sleep(1)
        buttonElement = driver.find_element_by_id("LoginUser_btnLogin")
        time.sleep(1)
        buttonElement.click()
        time.sleep(2)
        linkUnlock = driver.find_element_by_link_text("Unlock").click()
        time.sleep(2)

        self.iterateFile(driver)

        print("Finish")
        driver.close()

    def iterateFile(self, driver):
            
        with open(self.filename, "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()   
                print(stripped_line)
                inputElement = driver.find_element_by_id("txtUlkNumero")
                inputElement.send_keys(stripped_line)
                time.sleep(2)
                linkUnlock = driver.find_element_by_id("btnExecuteUlk").click()
                time.sleep(2)
                statusUnblock = driver.find_elements_by_xpath('.//span[@id = "lblAlertUlk"]')[0].text
                print(statusUnblock)
                driver.find_element_by_id('txtUlkNumero').clear()
                time.sleep(1)

exec = Essential()
exec.set_config_run()