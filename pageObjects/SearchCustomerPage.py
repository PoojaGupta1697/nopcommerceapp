class SearchCustomer:

    txtEmail_xpath="//*[@id='SearchEmail']"
    txtFirstName_xpath="//*[@id='SearchFirstName']"
    txtLastName_xpath="//*[@id='SearchLastName']"
    btnSearch_xpath="//*[@id='search-customers']"
    tblSearchResults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):  # constructor
        self.driver = driver


    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)
    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def clickOnSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return(len(self.driver.find_element_by_xpath(self.tableRows_xpath)))

    def getNoOfColumns(self):
        return(len(self.driver.find_element_by_xpath(self.tableColumns_xpath)))

    def SearchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid= table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text()
            if emailid == email:
                flag=True
                break
            return flag

    def SearchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name= table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text()
            if name ==Name:
                flag = True
                break
            return flag
