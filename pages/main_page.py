from pages.base_page import BasePage
from pages.locators import MainPageLocators, ProductPageLocators


class MainPage(BasePage):
    from .base_page import BasePage
    from .login_page import LoginPage
    from .locators import MainPageLocators

    class MainPage(BasePage):

        def __init__(self, *args, **kwargs):
            super(MainPage, self).__init__(*args, **kwargs)


    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     # alert = self.browser.switch_to.alert
    #     # alert.accept()
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    #
