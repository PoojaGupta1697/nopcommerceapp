
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
       driver= webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
       print("******launching chrome browser")
    elif browser=='firefox':
         driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver-v0.27.0-win64\geckodriver.exe")
         print("******launching firefox browser")
    return driver

def pytest_addoption(parser):    #get calues from hooks/cli
     parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#hook for adding environment info to the html reports
def pytest_configure(config):
    config._metadata['Project name']= 'nop commerce'
    config._metadata['module name'] ='customer'
    config._metadata['tester'] = 'Pooja'

#delete/modify environ info to html reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("plugins", None)

