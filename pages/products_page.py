from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Products_page(Base_page):
    PDP_BUTTONS = (By.CLASS_NAME, 'vim d-vi-region x-atf-center-river--buybox')
    PDP_PRODUCT_TITLE = (By.CLASS_NAME, 'x-item-title__mainTitle')
    ADD_TO_CART = (By.CLASS_NAME, 'vim x-atc-action overlay-placeholder')
    PDP_URL = "https://www.ebay.com/itm/125593649698?hash=item1d3df70222:g:bjAAAOSwyP5aMhN2&amdata=enc%3AAQAIAAAA0PyAVP4O3%2Bf88DhygF2xC81KBf4fhWjiCu49Hl7vQrDz93xB7SEIYo4HVPl3T7XZGIomw67QkUs3seA81W%2Fi%2BlmWmCG1Py%2FoVNpbfpnASmWcpaJtbSyebzMTqJy09lNHwN8m%2FfHjXhL74ILfVl7KzXekoMwAFzAhAByXdFdv60SyLsbPxD7Qejcd%2BGEQGAoCe%2F10xu4ehkxMBhVgFAZkZyo8ddnnAlD17PrMhcQRMCtToqvCM749L2m5Rr42C3mIFKlKHbVIb1g%2F5sXCD8KHPRI%3D%7Ctkp%3ABFBMkLDGsvZi"

    def product_has_info(self):
        self.chrome.has_detailed_information(*self.PDP_BUTTONS, *self.PDP_PRODUCT_TITLE)
        sleep(2)

    def add_to_cart(self):
        self.chrome.select_button(*self.ADD_TO_CART).click()
        sleep(2)

    def go_to_pdp(self):
        self.chrome.get(self.PDP_URL)
        sleep(2)
