from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page


class Advanced_search_page(Base_page):
    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.XPATH, '//*[@id="_nkw"]')
    KEYWORD_OPTIONS = (By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
    SEARCH_CATEGORY = (By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='field adv-keywords__btn-help']/child::button[@type='submit']")

    def enter_keywords_or_item_number(self, search_term):
        self.chrome.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys(search_term)

    available_keyword_options = []

    def select_next_keyword_option(self):
        keyword_dropdown = Select(self.chrome.find_element(*self.KEYWORD_OPTIONS))
        if not self.available_keyword_options:
            self.available_keyword_options = [option.text for option in keyword_dropdown.options]
        selected_option = self.available_keyword_options.pop(0)
        keyword_dropdown.select_by_visible_text(selected_option)
        print(f"Selected keyword option: {selected_option}")

    def select_search_category(self, category):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORY))
        category_dropdown.select_by_visible_text(category)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
