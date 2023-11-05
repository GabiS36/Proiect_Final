from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Cart_page(Base_page):
    CART_PAGE_TITLE = (By.CLASS_NAME, "main-title font-title-1")
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "//span[text()='You don't have any items in your cart.']")
    EMPTY_CART_GUEST = (By.CLASS_NAME, "//span[text()='Have an account? Sign in to see your items.']")
    GO_TO_CHECKOUT_BUTTON = (By.CLASS_NAME, "cart-summary-call-to-action")

    def check_empty_cart_URL(self):
        self.check_page_url('https://cart.payments.ebay.com/')

    def check_product_in_cart(self):
        prod_in_cart = self.wait_for_elem_by_selector(*self.GO_TO_CHECKOUT_BUTTON)
        self.assertTrue(prod_in_cart.is_display(), 'Product not in cart')







