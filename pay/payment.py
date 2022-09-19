from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("Please enter you card number: ")  # valid number: 1249190007575069
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    payment_processor = PaymentProcessor("9aa2040c-9a53-4654-a5d2-15221f90d9da")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()
