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

    @pytest.mark.sanity
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


        self.email= random_generator() +"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Pooja")
        self.addcust.setLastName("Gupta")
        self.addcust.setGender("Female")
        self.addcust.setDob("09/16/1997")
        self.addcust.setCompanyName("BusyQA")
        self.addcust.setAdminContent("This s for testing")
        self.addcust.setMgrOfVendor("Not a vendor")
        self.addcust.setCustomerRole("Registered")
        self.addcust.clickOnSave()
        self.logger.info("***********Saving Customer Info ************")

        self.logger.info("***********Add Customer validation started************")
        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if ' customer has been added successfully' in self.msg:
            assert True==True
            self.logger.info("******Add customer Test passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.info("******Add customer Test failed*************")
            assert True==False
        self.driver.close()
        self.logger.info("**********Ending Add Customer Test*********")

def random_generator(size=8,chars=string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))



