from behave import *


@then('Cart: I verify the cart page URL is correct')
def step_impl(context):
    context.cart_object.check_empty_cart_URL()


@then('Cart: the selected product should be added to the shopping cart')
def step_impl(context):
    context.cart_object.check_product_in_cart()
