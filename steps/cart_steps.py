from behave import *


@given('Cart: the user is on the cart page with products added')
def step_impl(context):
    context.cart_object.go_to_pdp()
    context.cart_object.accept_cookies()
    context.cart_object.add_to_cart()


@then('Cart: I verify the cart page URL is correct')
def step_impl(context):
    context.cart_object.check_empty_cart_URL()


@then('Cart: the selected product should be added to the shopping cart')
def step_impl(context):
    context.cart_object.check_product_in_cart()


@then('Cart: I check that the subtotal is correct {expected_price}')
def step_impl(context, expected_price):
    context.cart_object.check_subtotal(expected_price)


@then('Cart: I check that the cart icon in the header displays the correct number of products: {1}')
def step_impl(context, expected_count):
    context.cart_object.check_icon_count(expected_count)


@when('Cart: I click the Remove link')
def step_impl(context):
    context.cart_object.click_remove_link()


@then('Cart: I check the empty cart message')
def step_impl(context):
    context.cart_object.check_empty_cart_message()
