from browser import Browser
from pages.ebay_advanced_search_page import Advanced_search_page
from pages.cart_page import Cart_page
from pages.ebay_homepage import Home_page
from pages.products_page import Products_page


def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.advanced_search_object = Advanced_search_page()
    context.cart_object = Cart_page()
    context.products_object = Products_page()


def after_all(context):
    context.browser.close()
