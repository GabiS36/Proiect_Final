from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Home_page(Base_page):

    SEARCH_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")
    SEARCH_CATEGORIES = (By.ID, "gh-cat")
    ADVANCED_SEARCH_LINK = (By.ID, "gh-as-a")
    SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="BOLD"][1]')
    HOMEPAGE_URL = "https://www.ebay.com/"
    CART_ICON = (By.XPATH, '//*[@id="gh-minicart-hover"]')
    CART_ICON_DIALOG_TITLE = (By.XPATH, '//h2[text()="Your cart is empty"]')
    CART_ICON_DIALOG_MESSAGE = (By.XPATH, '//span[text()="Time to start shopping!"]')
    GUEST_ID = (By.CLASS_NAME, "gh-ug-guest")
    PRODUCT = (By.XPATH, '//img[@alt="NEW Black Gel Pen Full Matte Water 0.5 Pens Writing Stationery Supply Office"]')

    def navigate_to_homepage(self):
        self.chrome.get(self.HOMEPAGE_URL)

    def insert_search_value(self, query):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys(query)
        sleep(1)

    def choose_category(self, category_name):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category_name)
        sleep(1)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_search_results(self, no_of_results):
        no_results = self.chrome.find_element(*self.SEARCH_RESULTS).text
        result = no_results.replace(",", "")
        assert int(result) >= int(no_of_results), f"ERROR: No of Results is incorrect. Expected: {no_of_results}, " \
                                                  f"ACTUAL {result}"

    def click_advanced_search_link(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_LINK).click()

    def hover_over_cart_icon_header(self):
        elem = self.chrome.find_element(*self.CART_ICON)
        self.hover_by_elem(elem)
        sleep(3)

    def check_empty_cart_icon_dialog_title(self):
        self.chrome.find_element(*self.CART_ICON_DIALOG_TITLE)

    def click_cart_icon_header(self):
        self.chrome.find_element(*self.CART_ICON).click()

    def check_guest(self):
        self.check_element_is_displayed(*self.GUEST_ID)
        sleep(3)

    def select_products(self):
        self.select_product(*self.PRODUCT)
        sleep(3)

    def navigate_product_results_url(self):
        self.chrome.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=pen&_sacat=0')
        sleep(4)
