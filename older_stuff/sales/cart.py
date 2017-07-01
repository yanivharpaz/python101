class Cart:
    def __init__(self):
        self._contents = dict()

    def process(self, order):
        if order.add:
            if not order.item in self._contents:
                self._contents[order.item] = 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                if self._contents[order.item] > 1:
                    self._contents[order.item] -= 1
                else:
                    self._contents.pop(order.item)

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__, self._contents)
