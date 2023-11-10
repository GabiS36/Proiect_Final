from behave import *


@given('Home page: I am a user on ebay home page')
def step_impl(context):
    context.home_page_object.navigate_to_homepage()
    context.home_page_object.accept_cookies()


@when('Home page: I hover the cart icon in the header')
def step_impl(context):
    context.home_page_object.hover_over_cart_icon_header()


@When('Home page: I search for "{query}" from category "{category_name}"')
def step_impl(context, query, category_name):
    context.home_page_object.insert_search_value(query)
    context.home_page_object.choose_category(category_name)
    context.home_page_object.click_search_button()


@then('Home page: I have at least "{no_of_results}" results returned')
def step_impl(context, no_of_results):
    context.home_page_object.check_search_results(no_of_results)


@when('Home page: I click on the advanced link')
def step_impl(context):
    context.home_page_object.click_advanced_search_link()


@then('Home page: I verify empty cart icon dialog title')
def step_impl(context):
    context.home_page_object.check_empty_cart_icon_dialog_title()


@when('Home page: I click the cart icon in the header')
def step_impl(context):
    context.home_page_object.click_cart_icon_header()


@when('Home page: the user is on the product results page')
def step_impl(context):
    context.home_page_object.navigate_product_results_url()


@when('Home page: the user selects a product and a new tab opens')
def step_impl(context):
    context.home_page_object.select_products()
    context.home_page_object.switch_tab()
