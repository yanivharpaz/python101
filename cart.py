

def get_order():
    line = input('[command] [item] ===> ')
    command = line[0]
    item = line[2:]
    order = dict()
    order['command'] = command
    order['item'] = item
    return order

def add_to_cart(item, cart):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1


def remove_from_cart(item, cart):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
        else:
            cart.pop(item, None)
    else:
        print(item, 'does not exist in cart, nothing removed.')
        return False

    return True


def go_shopping():
    print("Hello there.")
    print("Usage: [command]: a -> add  d -> delete  q -> quit")
    cart = dict()

    while True:
        print('Just to see what is going on', cart)
        order = get_order()
        if order['command'] == 'q':
            break
        elif order['command'] == 'a':
            add_to_cart(order['item'], cart)
            print(order['item'], 'added.')
        elif order['command'] == 'd':
            if remove_from_cart(order['item'], cart):
                print(order['item'], 'removed.')

    print(cart)
    print('thank you for shopping with us')


def main():
    go_shopping()

if __name__ == '__main__':
    main()