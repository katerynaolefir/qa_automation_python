from core.ui.sause_demo.locators.product_detail_page import ProductDetailPageLocators
from core.ui.sause_demo.pages.base_page import BasePage
from utils.settings import d_settings

class ProductDetailsPage(BasePage):
    def __init__(self, page, product_id):
        super().__init__(page, base_url=d_settings.SAUSE_DEMO_BASE_URL)
        self.full_url = f'collections/frontpage/products/{product_id}'
        

        self.locators = ProductDetailPageLocators

    def is_page_loaded(self):
        return all([self.about_us_footer_status(), self.about_us_text()])


    def _product_form(self):
        locator = self.page.locator('#product-form')
        locator.is_visible(timeout=3*1000)
        return locator


    def get_product_name(self):
        return self._product_form().locator('h1').text_content().strip()


    def get_product_price(self):
        return self._product_form().locator('h2 span').text_content().strip()


    def about_us_footer_status(self):
        return self.page.locator(self.locators.about_us_text_loc).is_visible(timeout=3 * 1000)

    def about_us_text(self):
        return self.page.locator(self.locators.about_us_text_loc).text_content().strip()


    def add_product_to_cart_btn_status(self):
        return self.page.locator(self.locators.add_product_to_cart_btn_loc).is_visible()


    def add_product_to_cart_btn_text(self):
        return self.page.locator(self.locators.add_product_to_cart_btn_loc).input_value()


    def click_add_product_to_cart(self):
        self.page.locator(self.locators.add_product_to_cart_btn_loc).click()