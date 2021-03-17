import pytest

from pages.product_page import ProductPage


@pytest.mark.skip
def test_user_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_correct_product()
    page.should_be_correct_sum()


@pytest.mark.skip
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                                  pytest.param(
                                      'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                                      marks=pytest.mark.xfail),
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
@pytest.mark.skip
def test_guest_can_add_product_to_basket_bug(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_correct_product()
    page.should_be_correct_sum()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, product_url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_disappeared()
