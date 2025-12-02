from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    driver.find_element("id","button not exists")
except NoSuchElementException as nse:
    print("no such element",nse.msg)
