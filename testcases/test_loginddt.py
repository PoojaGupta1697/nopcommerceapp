import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperites import readConfig
from utilities.customlogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseURL= readConfig.getApplicationURL()
    path=".//Testdata/xltestdata.xlsx"
    logger =LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("****Test_002_DDT_Login")
        self.logger.info("**********verify login_ddt test*************")
        self.driver= setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=ExcelUtils.getRowCount(self.path,'Sheet1')
        print("no.of rows in excel",self.rows)

        lst_status=[]     #empty list variable

        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readdata(self.path, 'Sheet1',r,1)
            self.password=ExcelUtils.readdata(self.path, 'Sheet1',r,2)
            self.exp =ExcelUtils.readdata(self.path, 'Sheet1',r,3)


            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title= "Dashboard/nopCommerce administration"

            if act_title==exp_title:
               if self.exp=="Pass":
                  self.logger.info("******passed")
                  self.lp.clickLogout()
                  lst_status.append("pass")
               elif self.exp == "fail":
                    self.logger.info("*********failed*****")
                    self.lp.clickLogout()
                    lst_status.append("fail")


            elif act_title!= exp_title:
                 if self.exp=='Pass':
                    self.logger.info("********failed*****")
                    lst_status.append("Fail")
                 elif self.exp == 'fail':
                      self.logger.info("*********passed****")
                      lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**********login ddt test passed****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********login ddt test failed****")
            self.driver.close()
            assert False

        self.logger.info("end of login ddt test")
        self.logger.info("completed test_002_login_ddt")


