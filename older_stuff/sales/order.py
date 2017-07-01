class Order:
    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        line = input('[command] [item] ===> ')
        command = line[0]
        item = line[2:]
        if command == 'q':
            self.quit = True
        elif command == 'a':
            self.add = True
        elif command == 'd':
            self.delete = True
        self.item = item
