from behave import *


@when('Advanced search page: I type "{search_term}" in the enter keyword textbox')
def step_impl(context, search_term):
    context.advanced_search_object.enter_keywords_or_item_number(search_term)


@when('Advanced search page: I select a keyword option from keyword options')
def step_impl(context):
    context.advanced_search_object.select_next_keyword_option()


@when('Advanced search page: I choose "{category}" from the category list')
def step_impl(context, category):
    context.advanced_search_object.select_search_category(category)


@when('Advanced search page: I click search button')
def step_impl(context):
    context.advanced_search_object.click_search_button()
