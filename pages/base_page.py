from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser


class Base_page(Browser):
    COOKIES_BUTTON = (By.ID, "gdpr-banner-accept")

    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.COOKIES_BUTTON).click()
        except:
            pass

    def check_element_is_displayed(self, by, selector):
        element = self.chrome.find_element(by, selector)
        self.assertTrue(element.is_displayed(), 'Element not displayed')

    def hover_by_elem(self, elem):
        actions = ActionChains(self.chrome).move_to_element(elem)
        actions.perform()

    def check_page_url(self, expected_url):
        actual = self.chrome.current_url
        self.assertEqual(expected_url, actual, 'URL is incorrect')

    def wait_and_click_element_by_selector(self, by, selector):
        print(f"Waiting for element using {by} and {selector}")
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((by, selector)))
        element = self.chrome.find_element(by, selector)
        if not element.is_displayed():
            print("Element is not displayed.")
        element.click()

    def has_detailed_information(self, by, selector):
        product_details = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
        self.assertTrue(product_details.is_displayed(), 'Details are not displayed')

    def select_product(self, by, selector):
        product = self.chrome.find_element(by, selector)
        product.click()

    def switch_tab(self):
        self.chrome.switch_to.window(self.chrome.window_handles[1])

    def click_link(self, by, selector):
        link_element = WebDriverWait(self.chrome, 15).until(EC.element_to_be_clickable((by, selector)))
        link_element.click()
