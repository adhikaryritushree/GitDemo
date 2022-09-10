from selenium.webdriver.common.by import By


class Homepage:
    search = (By.XPATH, "//input[@class='search-keyword']")
    veggie = (By.XPATH, "//div[@class='products']/div")
    cart = (By.CSS_SELECTOR, ".cart-icon")
    proceed = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def addtocart(self):
        self.driver.find_element(*Homepage.search).send_keys('cu')

    def addveggies(self):
        products = self.driver.find_elements(*Homepage.veggie)
        for product in products:
            product.find_element(By.CSS_SELECTOR, ".product-action").click()

    def clickcart(self):
        self.driver.find_element(*Homepage.cart).click()

    def tocheckout(self):
        return self.driver.find_element(*Homepage.proceed)



