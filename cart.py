import sales.order, sales.cart

def go_shopping():
    print("Hello there.")
    print("Usage: [command]: a -> add  d -> delete  q -> quit")
    cart = sales.cart.Cart()
    order = sales.order.Order()
    order.get_input()

    while not order.quit:
        cart.process(order)
        order = sales.order.Order()
        order.get_input()

    print(cart)


def main():
    go_shopping()


if __name__ == '__main__':
    main()