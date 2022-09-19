from pay.order import LineItem, Order
from pay.payment import pay_order


def main() -> None:
    order = Order()
    order.line_items.append(LineItem(name="shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Gat", price=50_00))
    pay_order(order)


if __name__ == "__main__":
    main()
