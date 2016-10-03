

def get_order():

    line = input('[command] [item] ===> ')
    command = line[0]
    item = line[2:]
    order = {}
    order['command'] = command
    order['item'] = item

    return order


def go_shopping():
    print("Hello there.")
    print("Usage: [command]: a -> add  d -> delete  q -> quit")
    cart = []

    while True:
        order = get_order()
        if order['command'] == 'q':
            break
        elif order['command'] == 'a':
            cart.append(order['item'])
            print(order['item'], 'added.')
        elif order['command'] == 'd':
            cart.remove(order['item'])
            print(order['item'], 'removed.')

    print(cart)
    print("thank you for shopping with us")


def main():
    go_shopping()

if __name__ == "__main__":
    main()