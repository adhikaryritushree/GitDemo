from selenium.webdriver.common.by import By


class CartPage:

    promo = (By.CSS_SELECTOR, ".promoCode")
    apply = (By.CSS_SELECTOR, ".promoBtn")
    totalamt = (By.CSS_SELECTOR, ".totAmt")
    dscntamt = (By.CSS_SELECTOR, ".discountAmt")
    placeorder = (By.XPATH, "//button[contains(text(), 'Place Order')]")

    def __init__(self, driver):
        self.driver = driver

    def enterpromo(self):
        self.driver.find_element(*CartPage.promo).send_keys('rahulshettyacademy')

    def applypromo(self):
        self.driver.find_element(*CartPage.apply).click()

    def checkdiscount(self):
        totalamount = self.driver.find_element(*CartPage.totalamt).text
        discountamount = self.driver.find_element(*CartPage.dscntamt).text
        tot = int(totalamount)
        dsc = float(discountamount)
        if tot >= dsc:
            print("you have received the discount. Yay!")
        else:
            print("Better luck next time!")

    def orderplaced(self):
        self.driver.find_element(*CartPage.placeorder).click()







