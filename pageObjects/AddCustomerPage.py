import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomers_menu_xpath="/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    btnAddnew_xpath="/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"
    txtEmail_xpath="//*[@id='Email']"
    txtPassword_Xpath="//*[@id='Password']"
    txtFirstName_xpath="//*[@id='FirstName']"
    txtLastname_Xpath="//*[@id='LastName']"
    rdMaleGender_id="//*[@id='Gender_Male']"
    rdFemaleGender_id="//*[@id='Gender_Female']"
    txtDob_xpath="//*[@id='DateOfBirth']"
    txtCompanyName_xpath="//*[@id='Company']"
    txtCustomerRoles_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath="//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[contains(text(),'ForumModerators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpMgrOfVendor_xpath="//*[@id='VendorId']"
    txtAdminContent_xpath="//*[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"
    #txtNewsletter_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    #lstitemYourstorename_xpath = "//li[contains(text),'Your store name')]"
    #lstitemTeststore2_xpath = "//li[contains(text),'Test store 2')]"

    def __init__(self, driver):  # constructor
        self.driver = driver


    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()


    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_Xpath).send_keys(password)



    def setCustomerRole(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':

            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li[2]/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();",self.listitem)


    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastname_Xpath).send_keys(lname)
    def setGender(self,gender):
        if gender == 'Male':
           self.driver.find_element_by_xpath(self.rdMaleGender_id).click()
        elif gender == 'Female':
           self.driver.find_element_by_xpath(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()
    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)
    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setMgrOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpMgrOfVendor_xpath))
        drp.select_by_visible_text(value)
    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()