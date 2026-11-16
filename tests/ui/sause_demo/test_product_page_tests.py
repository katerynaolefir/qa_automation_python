from allure_commons.types import AttachmentType
from assertpy import soft_assertions, assert_that
import pytest
from definitions import SCREENSHOTS_DIR
import time
from datetime import datetime
import allure


from utils.settings import d_settings

header_search_loc = '//div[@class="container upper"]//nav//a[text()="Search"]'
side_menu_loc = '#main-menu'
product_cards_block_loc = '.product-grid'
product_cards_loc = '.product-grid div'

product_cards_details_name = ''


@pytest.fixture(scope='function')

def home_page(browser, request):

    with allure.step('Open page'):
        page = browser.new_page()
        page.goto(d_settings.SAUSE_DEMO_BASE_URL)

    yield page
    # request.node.name - имя теста
    with allure.step('Take screenshots of the page after the test'):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        attach_file_screenshot = f"{request.node.name}--{timestamp}.png"

        page.screenshot(path=SCREENSHOTS_DIR / attach_file_screenshot, full_page=True)

        allure.attach.file(SCREENSHOTS_DIR / attach_file_screenshot, name='screenshot', attachment_type=AttachmentType.PNG)

    with allure.step('Close page'):
        page.close()

@allure.epic('Sauce Demo project')
@allure.feature('Sauce Demo old tests')
@allure.story('Rewritten test smoke')
@pytest.mark.ui
@pytest.mark.old_style
def test_smoke_product_page(home_page):

    with allure.step('Check that the elements are visible'):
        header_is_vis = home_page.locator(header_search_loc).is_visible()
        side_menu_is_vis = home_page.locator(side_menu_loc).is_visible()
        product_cards_is_vis = home_page.locator(product_cards_block_loc).is_visible()

        with soft_assertions():
            assert_that(header_is_vis, f'Cant find header, {header_search_loc}').is_true()
            assert_that(side_menu_is_vis, f'Cant find side menu, {side_menu_loc}').is_true()
            assert_that(product_cards_is_vis, f'Cant find product cards, {product_cards_block_loc}').is_true()

    time.sleep(2)



@allure.epic('Sauce Demo project')
@allure.feature('Sauce Demo old tests')
@allure.story('Rewritten test about product cards')
@pytest.mark.ui
@pytest.mark.old_style
def test_product_page_contains_3_cards(home_page):

    with allure.step('Check that all 3 elements are on the page'):
        product_cards_is_vis = home_page.locator(product_cards_loc).all()
        assert_that(product_cards_is_vis, f'Cant find 3 product cards{product_cards_loc}').is_length(3)

