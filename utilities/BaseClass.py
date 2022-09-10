import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifycode(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler('C:\\Users\\RITUSHREE\\PycharmProjects\\PythonVegetableProject\\utilities\\filelog.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger




