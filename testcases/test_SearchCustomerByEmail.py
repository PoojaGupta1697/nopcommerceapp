import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperites import readConfig
from utilities.customlogger import LogGen
import time
import string
import random



class Test_004_SearchCustomerByEmail:
    baseURL= readConfig.getApplicationURL()
    username=readConfig.getUsername()
    password= readConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("***********Search customer by email*************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***********login succesful*************")
        self.logger.info("***********Starting Search Customer by email test ************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        searchcust= SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickOnSearch()
        status=searchcust.SearchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.driver.quit();