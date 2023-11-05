from behave import *


@given('Products: the user is on the product details page')
def step_impl(context):
    context.products_page_object.go_to_pdp()
    context.products_page_object.accept_cookies()


@when('Products: the user clicks on the "Add to Cart" button')
def step_impl(context):
    context.products_page_object.add_to_cart()


@then('Products: the user should see detailed information about the selected product')
def step_impl(context):
    context.products_page_object.product_has_info()



