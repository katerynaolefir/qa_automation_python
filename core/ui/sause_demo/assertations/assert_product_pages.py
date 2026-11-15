from assertpy import assert_that, soft_assertions

class AssertProductPages:


    def assert_main_page_name_price_is_equal_to_details_page(
            self, main_page_product_name, main_page_product_price, product_detail_page_name, product_detail_page_price):
        with soft_assertions():

            assert_that(main_page_product_name, f'Main page name is {main_page_product_name}'
                        ).is_equal_to(product_detail_page_name)
            assert_that(main_page_product_price, f'Main page price is {main_page_product_price}'
                        ).is_equal_to(product_detail_page_price)



    def assert_details_page_about_us_footer_text(self, is_details_page_loaded, about_us_is_vis, about_us_is_not_empty):
        with soft_assertions():
            assert_that(is_details_page_loaded, 'Product details page is not loaded').is_true()
            assert_that(about_us_is_vis, 'About us footer text is not visible').is_true()
            assert_that(about_us_is_not_empty, 'About us footer text is empty').is_not_empty()



    def assert_details_page_add_to_cart_btn(self, btn_is_visible, btn_text):
        with soft_assertions():
            assert_that(btn_is_visible, 'Add to Cart button is not visible').is_true()
            assert_that(btn_text, 'Wrong button text').is_equal_to('Add to Cart')


