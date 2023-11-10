import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class Base_page(Browser):
    COOKIES_BUTTON = (By.ID, "gdpr-banner-accept")
    EMPTY_CART_MESSAGE = ("You don't have any items in your cart.")

    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.COOKIES_BUTTON).click()
        except:
            pass

    def check_element_is_displayed(self, by, selector):
        element = self.chrome.find_element(by, selector)
        time.sleep(3)
        self.assertTrue(element.is_displayed(), 'Element not displayed')
        time.sleep(3)

    def hover_by_elem(self, elem):
        actions = ActionChains(self.chrome).move_to_element(elem)
        actions.perform()
        time.sleep(3)

    def check_page_url(self, expected_url):
        actual = self.chrome.current_url
        self.assertEqual(expected_url, actual, 'URL is incorrect')

    def wait_for_elem_by_selector(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))

    def wait_and_click_element_by_selector(self, by, selector):
        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
        self.chrome.find_element(by, selector).click()

    def select_button(self, by, selector):
        product_link = WebDriverWait(self.chrome, 10).until(EC.element_to_be_clickable((by, selector)))
        product_link.click()

    def has_detailed_information(self, by, selector):
        product_details = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
        self.assertTrue(product_details.is_displayed(), 'Details are not displayed')

    def select_product(self, by, selector):
        product = self.chrome.find_element(by, selector)
        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(self.chrome, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda d: product)
        product.click()
        time.sleep(2)

    def switch_tab(self):
        self.chrome.switch_to.window(self.chrome.window_handles[1])
