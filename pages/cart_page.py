from time import sleep
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Base_page


class Cart_page(Base_page):
    CART_PAGE_TITLE = (By.CLASS_NAME, "main-title font-title-1")
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, 'font-title-3')
    GO_TO_CHECKOUT_BUTTON = (By.XPATH, "//*[@id='mainContent']/div/div[3]/div[2]/div/div[1]/button")
    QTY_OPTIONS = (By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div[1]/div/ul/li/div/div/div/div[1]/div/div['
                             '3]/div/div[1]/div[1]/div/span/span')
    ADD_TO_CART = (By.XPATH, '//*[@id="mainContent"]/div[2]/div/div[1]/div[2]/ul/li[2]/div/a')
    SUBTOTAL_HIGH = (By. CLASS_NAME, 'cart-summary-line-item')
    REMOVE_LINK = (By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div[1]/div/ul/li/div/div/div/div[2]/span['
                             '2]/button')
    ICON_COUNT = (By.ID, "gh-cart-n")
    CART_URL = 'https://cart.payments.ebay.com/'
    PDP_URL = 'https://www.ebay.com/itm/126136404933?hash=item1d5e50cbc5:g:qTYAAOSwmlVlKYTL&amdata=enc' \
              '%3AAQAIAAAA0Arorp1xQmfIbg4yo4s8tUpSfo3Mghlsr%2BSYnKDk%2B%2FqfMQscMMZ48LJbsIAe%2BoPP6uuKmyp5X1ev%2By8' \
              '%2Fm5vn0HRfdrl%2Bney73qNiSFYPTTa2F3%2F9uVVtjOjjCHM0Jb7jHUGVb9J%2FoVFKrOtlYocOIx2vBVG65JMYTLRHEu353%2By' \
              '%2Ft5qB72IxfytK0bH89e0Jd6uaqDVKbTvMN%2F%2FwvYPR7jFcIXsj7MgIesHJyHEyxWnUo9QwhrEhQV6nMC8CE5oGM' \
              '%2B0hhaWenAlj9HRqVFDGudU%3D%7Ctkp%3ABFBMurOxhPdi'

    def check_empty_cart_URL(self):
        self.check_page_url('https://cart.payments.ebay.com/')

    def go_to_cart(self):
        self.chrome.get(self.CART_URL)

    def check_product_in_cart(self):
        self.has_detailed_information(*self.GO_TO_CHECKOUT_BUTTON)

    def check_subtotal(self, expected_price):
        actual_text = self.chrome.find_element(*self.SUBTOTAL_HIGH).text.replace('Item (1)\n', '').strip()
        self.assertEqual(actual_text, expected_price, "Subtotal is incorrect")

    def check_icon_count(self, expected_count):
        try:
            WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ICON_COUNT))
            actual_count = self.chrome.find_element(*self.ICON_COUNT).text.strip()
            assert actual_count == expected_count, \
                f"Product Count is incorrect. Expected: {expected_count}, Actual: {actual_count}"
        except TimeoutException:
            print("Timed out waiting for icon count element to be present.")

    def click_remove_link(self):
        self.click_link(*self.REMOVE_LINK)

    def check_empty_cart_message(self):
        try:
            self.check_element_is_displayed(*self.EMPTY_CART_MESSAGE)
        except StaleElementReferenceException:
            print("Stale element reference. Refresh the page or handle it accordingly.")

    def go_to_pdp(self):
        self.chrome.get(self.PDP_URL)
        sleep(2)

    def add_to_cart(self):
        try:
            self.wait_and_click_element_by_selector(*self.ADD_TO_CART)
        except TimeoutException as e:
            print(f"TimeoutException: {e}")
            print(f"Failed to click 'Add to Cart' button within the specified timeout.")
            raise
        sleep(2)
