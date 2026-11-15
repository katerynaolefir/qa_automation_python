import allure
from allure_commons.types import AttachmentType
from assertpy import soft_assertions, assert_that
import pytest
from definitions import SCREENSHOTS_DIR
import time
from datetime import datetime
from utils.settings import d_settings
from random import choice

from core.ui.sause_demo.assertations.assert_product_pages import AssertProductPages
from core.ui.sause_demo.pages.product_page import ProductPage

product_asserts = AssertProductPages()

@pytest.fixture(scope='module')
def page(browser, request):

    page = browser.new_page()
    yield page
    with allure.step('Take screenshots of the page after the test'):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        attach_file_screenshot = f"{request.node.name}--{timestamp}.png"

        page.screenshot(path=SCREENSHOTS_DIR / attach_file_screenshot, full_page=True)

        allure.attach.file(SCREENSHOTS_DIR / attach_file_screenshot, name='screenshot', attachment_type=AttachmentType.PNG)



@pytest.fixture(scope='module')
def product_page(page):
    return ProductPage(page)

@allure.epic('Sauce Demo project')
@allure.feature('Sauce Demo modern tests')
@allure.story('Smoke test')
@pytest.mark.ui
@pytest.mark.modern
def test_smoke_product_page(product_page):
    with allure.step('Open page and check that is loaded'):
        product_page.open()

        assert_that(product_page.is_page_loaded(), 'Page is not loaded').is_true()


@allure.epic('Sauce Demo project')
@allure.feature('Sauce Demo modern tests')
@allure.story('Smoke test')
@pytest.mark.ui
@pytest.mark.modern
def test_product_page_cards_with_details_page(product_page):
    with allure.step('Open page'):
        product_page.open()

    with allure.step('Choosing a Card (name, price)'):
        product_cards = product_page.get_list_of_all_product_cards()

        product_el = choice(product_cards)

        main_page_product_name = product_page.get_product_name_from_card(product_el)
        main_page_product_price = product_page.get_product_price_from_card(product_el)

    with allure.step('Open details page and check name and price on main and details pages'):
        details_page = product_page.open_random_product_card_details(product_el)
        product_detail_page_name = details_page.get_product_name()
        product_detail_page_price = details_page.get_product_price()

        product_asserts.assert_main_page_name_price_is_equal_to_details_page(
            main_page_product_name, main_page_product_price, product_detail_page_name, product_detail_page_price
        )


@allure.epic('Sauce Demo project')
@allure.feature('Sauce Demo modern tests')
@allure.story('Footer test')
@pytest.mark.ui
@pytest.mark.modern
def test_about_us_footer_text_displayed(product_page):
    with allure.step('Open page'):
        product_page.open()

    with allure.step('Open details page and check that footer text displayed'):
        product_el = choice(product_page.get_list_of_all_product_cards())
        details_page = product_page.open_random_product_card_details(product_el)


        product_asserts.assert_details_page_about_us_footer_text(
            details_page.is_page_loaded(),
            details_page.about_us_footer_status(),
            details_page.about_us_text(),
        )


@allure.epic('Sauce Demo project')
@allure.feature('Sauce Demo modern tests')
@allure.story('Cart test')
@pytest.mark.ui
@pytest.mark.modern
def test_add_product_to_cart(product_page):
    with allure.step('Open page'):
        product_page.open()

    with allure.step('Open details page and check "Add to Cart" button text on details page'):
        product_el = choice(product_page.get_list_of_all_product_cards())
        details_page = product_page.open_random_product_card_details(product_el)

        product_asserts.assert_details_page_add_to_cart_btn(
            details_page.add_product_to_cart_btn_status(),
            details_page.add_product_to_cart_btn_text(),
        )
    with allure.step('Click "Add to Cart" button'):
        details_page.click_add_product_to_cart()
    pass