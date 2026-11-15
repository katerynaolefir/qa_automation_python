from core.ui.sause_demo.locators.product_page import ProductPageLocators
from core.ui.sause_demo.pages.base_page import BasePage
from core.ui.sause_demo.pages.details_page import ProductDetailsPage
from utils.settings import d_settings
from random import choice

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page, base_url=d_settings.SAUSE_DEMO_BASE_URL)
        self.full_url = ''

        self.locators = ProductPageLocators

    def is_page_loaded(self):


        return all([self.header_el_status(), self.side_menu_status(), self.product_cards_status()])


    def header_el_status(self):
        return self.page.locator(self.locators.header_search_loc).is_visible(timeout=3 * 1000)

    def side_menu_status(self):
        return self.page.locator(self.locators.side_menu_loc).is_visible(timeout=3 * 1000)

    def product_cards_status(self):
        return self.page.locator(self.locators.product_cards_block_loc).is_visible(timeout=3 * 1000)

    def get_list_of_all_product_cards(self) -> list:
        return self.page.locator(self.locators.product_cards_block_card_loc).all()

    def get_product_name_from_card(self, product_locator) -> str:
        return product_locator.locator('h3').text_content().strip()

    def get_product_price_from_card(self, product_locator) -> str:
        return product_locator.locator('h4').text_content().strip()



    def open_random_product_card_details(self, product_locator) -> ProductDetailsPage:
        product_id = '-'.join(self.get_product_name_from_card(product_locator).split())
        product_locator.locator('a').click()

        return ProductDetailsPage(self.page, product_id)
