from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Advanced_search_page(Base_page):
    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.XPATH, '//*[@id="_nkw"]')
    KEYWORD_OPTIONS = (By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
    SEARCH_CATEGORY = (By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='field adv-keywords__btn-help']/child::button[@type='submit']")

    def enter_keywords_or_item_number(self):
        self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys("Pampers")

    def select_keywords_option(self):
        keyword_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
        keyword_dropdown.select_by_visible_text("Exact words, exact order")

    def select_search_category(self):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORY))
        category_dropdown.select_by_visible_text("Baby")

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
