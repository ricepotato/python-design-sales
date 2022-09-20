from pay.order import LineItem, Order
from pay.payment import pay_order


def main() -> None:
    card = input("Please enter you card number: ")  # valid number: 1249190007575069
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))

    order = Order()
    order.line_items.append(LineItem(name="shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Gat", price=50_00))
    pay_order(order)


if __name__ == "__main__":
    main()
