import time

from help_selectors.shoppingCartSelectors import *
from pages.base_page import BasePage


class ShoppingCart(BasePage):

    def close_demo_navigation(self):
        self.wait_for_element(CLOSE_DEMO_NAVIGATION_SELECTOR, 5).click()

    def store_product_name(self):
        time.sleep(1)
        return self.wait_for_element(SELECTED_PRODUCT_NAME_SELECTOR, 5).text

    def chose_size(self):
        self.wait_for_element(PRODUCT_FIRST_SIZE_SELECTOR, 5).click()

    def chose_color(self):
        self.wait_for_element(PRODUCT_FIRST_COLOR_SELECTOR, 56).click()

    def chose_quantity(self, value):
        self.type(QUANTITY_SELECTOR, value)

    def add_product_to_cart(self):
        self.wait_for_element(ADD_TO_CART_SELECTOR, 5).click()
        time.sleep(5)

    def verify_cart_page_url(self):
        time.sleep(5)
        return self.driver.current_url

    def restore_product_name(self):
        time.sleep(1)
        return self.wait_for_element(CART_PRODUCT_NAME_SELECTOR, 5).text

    def remove_items(self):
        self.action_chain(CART_SELECTOR)
        time.sleep(1)
        self.action_chain(SEE_DETAILS_SELECTOR)
        self.action_chain(REMOVE_ITEM_FROM_CART_SELECTOR)
        time.sleep(1)
        self.wait_for_element(REMOVE_ITEM_BUTTON_SELECTOR, 5).click()
        time.sleep(1)

    def close_shopping_cart_window(self):
        self.wait_for_element(CLOSE_SHOPPING_CART_WINDOW_SELECTOR, 5).click()

    def select_cart_menu(self):
        time.sleep(5)
        self.action_chain(CART_SELECTOR)
        time.sleep(1)

    def select_details_menu(self):
        self.action_chain(SEE_DETAILS_SELECTOR)

    def remove_item_from_cart(self):
        self.action_chain(REMOVE_ITEM_FROM_CART_SELECTOR)
        time.sleep(1)

    def click_remove_item_button(self):
        self.wait_for_element(REMOVE_ITEM_BUTTON_SELECTOR, 5).click()

    def get_removed_item_message(self):
        return self.get_element_text(DELETED_ITEMS_MESSAGE_SELECTOR)

    def store_product_base_price(self):
        i = 2
        product_price = self.wait_for_element(PRODUCT_FINAL_PRICE_SELECTOR, 5)
        current_price = product_price.text
        current_price_without_dollar = current_price.replace('$', '')
        actual_price = float(current_price_without_dollar)
        base_price = actual_price * i
        return base_price

    def store_product_subtotal_price(self):
        cart_product_price = self.wait_for_element(CART_PRODUCT_PRICE_SELECTOR, 5)
        cart_current_price = cart_product_price.text
        cart_current_price_without_dollar = cart_current_price.replace('$', '')
        subtotal_price = float(cart_current_price_without_dollar)
        return subtotal_price

    def calculate_product_total_price(self):
        i = 5

        cart_product_price = self.wait_for_element(CART_PRODUCT_PRICE_SELECTOR, 5)
        cart_current_price = cart_product_price.text
        cart_current_price_without_dollar = cart_current_price.replace('$', '')
        subtotal_price = float(cart_current_price_without_dollar)

        shipping_product_fee = self.wait_for_element(SHIPPING_FEE_SELECTOR, 5)
        shipping_current_fee = shipping_product_fee.text
        shipping_current_fee_without_dollar = shipping_current_fee.replace('$', '')
        shipping_value = float(shipping_current_fee_without_dollar)

        try:
            if i >= 3:
                discount_amount = self.wait_for_element(DISCOUNT_AMOUNT_SELECTOR, 5)
                discount_value = discount_amount.text
                discount_value_without_dollar = discount_value.replace('$', '')
                total_discount_value = float(discount_value_without_dollar)
                order_value = subtotal_price + total_discount_value
            else:
                order_value = subtotal_price
        except:
            order_value = subtotal_price

        order_price = order_value + shipping_value

        return order_price

    def store_product_total_value(self):
        total_price = self.wait_for_element(TOTAL_PRODUCT_PRICE_SELECTOR, 5)
        total_current_price = total_price.text
        total_current_price_without_dollar = total_current_price.replace('$', '')
        order_total = float(total_current_price_without_dollar)
        return order_total

    def click_edit_item_button(self):
        self.action_chain(EDIT_ITEM_IN_CART_SELECTOR)

    def change_the_size(self):
        self.wait_for_element(PRODUCT_SECOND_SIZE_SELECTOR, 5).click()

    def change_the_color(self):
        self.wait_for_element(PRODUCT_SECOND_COLOR_SELECTOR, 5).click()

    def change_the_quantity(self, value):
        self.type(QUANTITY_SELECTOR, value)

    def update_cart(self):
        self.wait_for_element(UPDATE_CART_SELECTOR, 5).click()

    def get_update_cart_message(self):
        return self.get_element_text(UPDATE_MESSAGE_SELECTOR)

    def insert_street_address(self, street):
        self.type(SHIPPING_STREET_SELECTOR, street)

    def insert_phone_number(self, phone):
        self.type(SHIPPING_PHONE_SELECTOR, phone)

    def check_billing_address(self):
        self.wait_for_element(CHECKBOX_BILLING_ADDRESS_SELECTOR, 5).click()

    def accept_terms(self):
        self.wait_for_element(ACCEPT_AGREEMENT, 5).click()

    def place_order(self):
        self.action_chain(PLACE_ORDER_SELECTOR)

    def get_confirmation_message(self):
        time.sleep(5)
        return self.get_element_text(THANKS_MESSAGE_SELECTOR)



