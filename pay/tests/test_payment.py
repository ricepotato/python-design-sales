from datetime import date
import pytest
from pay.order import LineItem, Order
from pay.payment import pay_order
from pay.credit_card import CreditCard


class PaymentProcessMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging {card} with amount ${amount/100:.2f}.")


def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, card, PaymentProcessMock())


def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        order = Order()
        pay_order(order, card, PaymentProcessMock())
