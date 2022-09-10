import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#from PageObject.CartPage import CartPage
from PageObject.CartPage import CartPage
from PageObject.CountryPage import CountryPage
from PageObject.homepage import Homepage
from utilities.BaseClass import BaseClass

class TestVeg(BaseClass):
    def test_vegincart(self):
        log = self.getlogger()
        home = Homepage(self.driver)
        home.addtocart()
        time.sleep(1)
        home.addveggies()
        home.clickcart()
        home.tocheckout().click()
        cartpg = CartPage(self.driver)
        cartpg.enterpromo()
        cartpg.applypromo()
        self.verifycode()
        txt = self.driver.find_element(By.XPATH, "//span[contains(text(),'Code applied ..!')]").text
        print(txt)
        log.info("Information generated")
        cartpg.checkdiscount()
        cartpg.orderplaced()
        country = CountryPage(self.driver)
        country.selectcounytry()
        country.selectcheckbox()
        country.proceedtobuy()
        print("Code changes after cloning")














