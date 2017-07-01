import older_stuff.sales.order


def go_shopping():
    print("Hello there.")
    print("Usage: [command]: a -> add  d -> delete  q -> quit")
    cart = older_stuff.sales.cart.Cart()
    order = older_stuff.sales.order.Order()
    order.get_input()

    while not order.quit:
        cart.process(order)
        order = older_stuff.sales.order.Order()
        order.get_input()

    print(cart)


def main():
    go_shopping()


if __name__ == '__main__':
    main()