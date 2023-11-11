from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Products_page(Base_page):
    PDP_PRODUCT_TITLE = (By.XPATH, '//*[@id="mainContent"]/div[1]/div[1]/h1')
    ADD_TO_CART = (By.XPATH, '//*[@id="mainContent"]/div[2]/div/div[1]/div[2]/ul/li[2]/div/a')
    PDP_URL = 'https://www.ebay.com/itm/126136404933?hash=item1d5e50cbc5:g:qTYAAOSwmlVlKYTL&amdata=enc%3AAQAIAAAA0Arorp1xQmfIbg4yo4s8tUpSfo3Mghlsr%2BSYnKDk%2B%2FqfMQscMMZ48LJbsIAe%2BoPP6uuKmyp5X1ev%2By8%2Fm5vn0HRfdrl%2Bney73qNiSFYPTTa2F3%2F9uVVtjOjjCHM0Jb7jHUGVb9J%2FoVFKrOtlYocOIx2vBVG65JMYTLRHEu353%2By%2Ft5qB72IxfytK0bH89e0Jd6uaqDVKbTvMN%2F%2FwvYPR7jFcIXsj7MgIesHJyHEyxWnUo9QwhrEhQV6nMC8CE5oGM%2B0hhaWenAlj9HRqVFDGudU%3D%7Ctkp%3ABFBMurOxhPdi'

    def product_has_info(self):
        self.has_detailed_information(*self.PDP_PRODUCT_TITLE)
        sleep(2)

    def add_to_cart(self):
        self.wait_and_click_element_by_selector(*self.ADD_TO_CART)
        sleep(2)

    def go_to_pdp(self):
        self.chrome.get(self.PDP_URL)
        sleep(2)
