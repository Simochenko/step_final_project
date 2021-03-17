from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CPASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_PRODUCT_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    SUM_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-default[href*='basket']")
    CART_LINK_INVALID = (By.CSS_SELECTOR, "#basket_unlink")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators():
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "#content_inner p")
    CART_TOTALS = (By.CSS_SELECTOR, "#basket_totals")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_URL_MARKER = 'login'
    REG_EMAIL = (By.ID, 'id_registration-email')
    REG_PWD1 = (By.ID, 'id_registration-password1')
    REG_PWD2 = (By.ID, 'id_registration-password2')
    REG_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    BASKET_SUM = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    # STRONG_NOFIFICATION = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    NOTIFICATION = (By.CSS_SELECTOR, '.alert-success .alertinner')
    PRODUCT_ADDED_MESSAGE = 'has been added to your basket.'
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')