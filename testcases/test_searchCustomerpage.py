import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperites import readConfig
from utilities.customlogger import LogGen
import time
import string
import random



class Test_003_AddCustomer:
    baseURL= readConfig.getApplicationURL()
    username=readConfig.getUsername()
    password= readConfig.getPassword()
    logger=LogGen.loggen()


    def test_AddCustomer(self,setup):
        self.logger.info("***********Test_001_Login*************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***********login succesful*************")
        self.logger.info("***********Starting Add Customer test ************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        self.logger.info("***********Providing Customer Info ************")

