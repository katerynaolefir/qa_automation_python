from allure import step
from core.ui.sause_demo.locators.product_detail_page import ProductDetailPageLocators
from core.ui.sause_demo.pages.base_page import BasePage
from utils.settings import d_settings

class ProductDetailsPage(BasePage):
    def __init__(self, page, product_id):
        super().__init__(page, base_url=d_settings.SAUSE_DEMO_BASE_URL)
        self.full_url = f'collections/frontpage/products/{product_id}'
        

        self.locators = ProductDetailPageLocators

    @step('Check that the page is loaded')
    def is_page_loaded(self):
        return all([self.about_us_footer_status(), self.about_us_text()])

    @step('Check that product form is visible')
    def _product_form(self):
        locator = self.page.locator('#product-form')
        locator.is_visible(timeout=3*1000)
        return locator

    @step('Get name of product card')
    def get_product_name(self):
        return self._product_form().locator('h1').text_content().strip()

    @step('Get price of product card')
    def get_product_price(self):
        return self._product_form().locator('h2 span').text_content().strip()

    @step('Check that footer text is visible')
    def about_us_footer_status(self):
        return self.page.locator(self.locators.about_us_text_loc).is_visible(timeout=3 * 1000)

    @step('Get footer text')
    def about_us_text(self):
        return self.page.locator(self.locators.about_us_text_loc).text_content().strip()

    @step('Check that "Add to Cart" button is visible')
    def add_product_to_cart_btn_status(self):
        return self.page.locator(self.locators.add_product_to_cart_btn_loc).is_visible()

    @step('Get value "Add to Cart" button')
    def add_product_to_cart_btn_text(self):
        return self.page.locator(self.locators.add_product_to_cart_btn_loc).input_value()

    @step('Click "Add to Cart" button')
    def click_add_product_to_cart(self):
        self.page.locator(self.locators.add_product_to_cart_btn_loc).click()