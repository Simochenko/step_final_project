import math
import re
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import ProductPageLocators


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        button.click()

    def get_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return None

    def get_num(self, how, what):
        try:
            numtxt = self.browser.find_element(how, what).text.replace(',', '.')
            return float(re.findall(r'\d+.\d+', numtxt)[0])
        except NoSuchElementException:
            return None

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
