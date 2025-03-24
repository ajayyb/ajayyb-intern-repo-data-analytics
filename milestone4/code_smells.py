def total_price(quantity):
    return quantity * 10

# 3 is magic number (random fixed number introduced) should be defined
    # as a constant in the code
DISCOUNT_RATE = 3
ITEM_THRESHOLD = 10

def calculate_total_price(quantity):
    if quantity > ITEM_THRESHOLD:
        return total_price(quantity) - (total_price(quantity) * DISCOUNT_RATE / 100)