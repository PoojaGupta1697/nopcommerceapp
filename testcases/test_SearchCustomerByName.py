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



class Test_005_SearchCustomerByName:
    baseURL= readConfig.getApplicationURL()
    username=readConfig.getUsername()
    password= readConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("***********Search customer by email*************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***********login succesful*************")
        self.logger.info("***********Starting Search Customer by name test ************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        searchcust= SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickOnSearch()
        status=searchcust.SearchCustomerByName("Victoria Terces")
        assert True==status
        self.driver.quit();