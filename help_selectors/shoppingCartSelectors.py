from selenium.webdriver.common.by import By

ACCEPT_AGREEMENT = (By.ID, "agreement__1")
ADD_TO_CART_SELECTOR = (By.XPATH, '//button[@type="submit" and @title="Add to Cart"]')
CART_PRODUCT_NAME_SELECTOR = (By.XPATH, '//strong[@class="product-item-name"]')
CART_PRODUCT_PRICE_SELECTOR = (By.XPATH, '//span[@class="cart-price"]')
CART_SELECTOR = (By.XPATH, '//a[@class="action showcart"]')
CHECKBOX_BILLING_ADDRESS_SELECTOR = (By.XPATH, '//input[@type="checkbox" and @name="billing-address-same-as-shipping"]')
CLOSE_DEMO_NAVIGATION_SELECTOR = (By.XPATH, '//button[@class="navigation-close" and @title="Close navigation"]')
CLOSE_SHOPPING_CART_WINDOW_SELECTOR = (By.XPATH, '//button[@class="action-close" and @data-role="closeBtn"]')
DELETED_ITEMS_MESSAGE_SELECTOR = (By.XPATH, '//span[contains(text(), "You have no items in your shopping cart.")]')
DISCOUNT_AMOUNT_SELECTOR = (By.XPATH, '//span[@data-th="checkout.sidebar.summary.totals.discount"]')
EDIT_ITEM_IN_CART_SELECTOR = (By.XPATH, '//div[@class="primary"]/a[@class="action edit" and @title="Edit item"]')
PLACE_ORDER_SELECTOR = (By.XPATH, '//div[@class="place-order-primary"]/button[@class="action primary checkout" and @type="button"]')
PRODUCT_FIRST_COLOR_SELECTOR = (By.XPATH, '(//div[@class="swatch-option color"])[1]')
PRODUCT_SECOND_COLOR_SELECTOR = (By.XPATH, '(//div[@class="swatch-option color"])[2]')
PRODUCT_FINAL_PRICE_SELECTOR = (By.XPATH, '//span[@data-price-type="finalPrice"]')
PRODUCT_FIRST_SIZE_SELECTOR = (By.XPATH, '(//div[@class="swatch-option text"])[3]')
PRODUCT_SECOND_SIZE_SELECTOR = (By.XPATH, '(//div[@class="swatch-option text"])[2]')
QUANTITY_SELECTOR = (By.XPATH, '//input[@type="number"]')
REMOVE_ITEM_BUTTON_SELECTOR = (By.XPATH, '//button[@class="action-primary action-accept"]')
REMOVE_ITEM_FROM_CART_SELECTOR = (By.XPATH, '//div[@class="secondary"]/a[@class="action delete" and @title="Remove item"]')
SEE_DETAILS_SELECTOR = (By.XPATH, '//span[@data-role="title" and @class="toggle"]/span[contains(text(), "See Details")]')
SELECTED_PRODUCT_NAME_SELECTOR = (By.XPATH, '//span[@itemprop="name"]')
SHIPPING_FEE_SELECTOR = (By.XPATH, '//span[@data-th="Shipping"]')
SHIPPING_PHONE_SELECTOR = (By.XPATH, '//input[@name="telephone"]')
SHIPPING_STREET_SELECTOR = (By.XPATH, '//input[@name="street[0]"]')
THANKS_MESSAGE_SELECTOR = (By.XPATH, '//h1[@class="page-title"]')
TOTAL_PRODUCT_PRICE_SELECTOR = (By.XPATH, '//strong/span[@data-bind="text: getValue()"]')
UPDATE_CART_SELECTOR = (By.XPATH, '//button[@type="submit" and @title="Update Cart"]')
UPDATE_MESSAGE_SELECTOR = (By.XPATH, '//div[contains(text(), "Geo Insulated Jogging Pant was updated in your shopping cart.")]')
