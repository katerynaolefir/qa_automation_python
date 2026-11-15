from assertpy import soft_assertions, assert_that
import pytest
from definitions import SCREENSHOTS_DIR
import time
from datetime import datetime
from random import choice

from utils.settings import d_settings

header_search_loc = '//div[@class="container upper"]//nav//a[text()="Search"]'
side_menu_loc = '#main-menu'
product_cards_block_loc = '.product-grid'
product_cards_loc = '.product-grid div'

product_cards_details_name = ''


@pytest.fixture(scope='function')

def home_page(browser, request):

    page = browser.new_page()
    page.goto(d_settings.SAUSE_DEMO_BASE_URL)
    yield page
    # request.node.name - имя теста

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    page.screenshot(path=SCREENSHOTS_DIR / f"{request.node.name}--{timestamp}.png", full_page=True)




@pytest.mark.ui
@pytest.mark.old_style
def test_smoke_product_page(home_page):

    header_is_vis = home_page.locator(header_search_loc).is_visible()
    side_menu_is_vis = home_page.locator(side_menu_loc).is_visible()
    product_cards_is_vis = home_page.locator(product_cards_block_loc).is_visible()

    with soft_assertions():
        assert_that(header_is_vis, f'Cant find header, {header_search_loc}').is_true()
        assert_that(side_menu_is_vis, f'Cant find side menu, {side_menu_loc}').is_true()
        assert_that(product_cards_is_vis, f'Cant find product cards, {product_cards_block_loc}').is_true()

    time.sleep(2)




@pytest.mark.ui
@pytest.mark.old_style
def test_product_page_contains_3_cards(home_page):

    product_cards_is_vis = home_page.locator(product_cards_loc).all()
    assert_that(product_cards_is_vis, f'Cant find 3 product cards{product_cards_loc}').is_length(3)


# @pytest.mark.ui
# @pytest.mark.old_style
# def test_product_page_cards_with_details_page(home_page):
#
#     product_cards = home_page.locator(product_cards_loc).all()
#
#     product_el = choice(product_cards)
#
#     main_page_product_name = product_el.locator('h3').text_content().strip()
#     main_page_product_price = product_el.locator('h4').text_content().strip()
#
#     product_el.locator('//a').click()
#
#     product_form = home_page.locator('#product-form')
#     product_details_page_name = product_form.locator('h1').text_content().strip()
#     product_details_page_price = product_form.locator('h2 span').text_content().strip()
#
#
#     with soft_assertions():
#         assert_that(main_page_product_name, f'Main page name is {main_page_product_name}'
#                     ).is_equal_to(product_details_page_name)
#         assert_that(main_page_product_price, f'Main page price is {main_page_product_price}'
#                     ).is_equal_to(product_details_page_price)