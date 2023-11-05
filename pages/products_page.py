from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Base_page


class Products_page(Base_page):
    PDP_BUTTONS = (By.CLASS_NAME, 'class="vim d-vi-region x-atf-center-river--buybox"')
    PDP_PRODUCT_TITLE = (By.CLASS_NAME, 'class="ux-textspans ux-textspans--BOLD"')
    ADD_TO_CART = (By.CLASS_NAME, 'vim x-atc-action overlay-placeholder')
    PDP_URL = "https://www.ebay.com/itm/375010219828?epid=27025553872&hash=item575059d734:g:3o0AAOSww-ZlOCzQ&amdata=enc%3AAQAIAAAA4JaRFkCxY6Ae9czdm7%2FDwVMzNToUn0F4mvwggaj3CnbR76HHuvEb3LC6iCd7gwIlwiwxfMR1mw9ntNvGWDR4t5HBO5JiFjKfXSl%2B%2FdlFJE72kmAcGrBq6RQc6MmBBn%2F0mg125f3NI7qs4ByNO6NC4KzJoRaWn2X130oAjtMOYQ%2BW%2B0Xc2xPYYTV2P8OSsPoLaZcKVYiOCJnxLj1FNXfHHjQaFfEXayZbMTYHkWuhttL%2BOzCR6VRVX4R68icuaa7Ld%2FZZstMr4vb1Zkz26ioyolex5uhm9sMynqkFz2vMncZr%7Ctkp%3ABFBMop-bkPRi"

    def product_has_info(self):
        self.chrome.has_detailed_information(*self.PDP_BUTTONS, *self.PDP_PRODUCT_TITLE)
        sleep(2)

    def add_to_cart(self):
        self.chrome.select_button(*self.ADD_TO_CART).click()
        sleep(2)

    def go_to_pdp(self):
        self.chrome.get(self.PDP_URL)
        sleep(2)

