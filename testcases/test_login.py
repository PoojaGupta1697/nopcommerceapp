import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperites import readConfig
from utilities.customlogger import LogGen

class Test_001_Login:
    baseURL= readConfig.getApplicationURL()
    username=readConfig.getUsername()
    password= readConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression

    def test_homepageTitle(self,setup):
        self.logger.info("***********Test_001_Login*************")
        self.logger.info("***********Verify homepageTitle*************")

        self.driver= setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***********home page title is passed*************")
        else:

            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("***********home page title is failed*************")
            assert False



    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self,setup):
        self.logger.info("**********verify login test*************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
             assert True
             self.logger.info("***********home page title is passed*************")
             self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"test_login.png")
            self.driver.close()
            self.logger.error("***********home page title is failed*************")
            assert False



