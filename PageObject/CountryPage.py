from selenium.webdriver.common.by import By


class CountryPage:
    select = (By.XPATH, "//div/select")
    checkbox = (By.CSS_SELECTOR, ".chkAgree")
    proceed = (By.XPATH, "//button[contains(text(), 'Proceed')]")


    def __init__(self, driver):
        self.driver = driver

    def selectcounytry(self):
        self.driver.find_element(*CountryPage.select).send_keys('India')

    def selectcheckbox(self):
        self.driver.find_element(*CountryPage.checkbox).click()

    def proceedtobuy(self):
        self.driver.find_element(*CountryPage.proceed).click()
