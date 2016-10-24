from pprint import pprint as pp


class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isupper():
            raise ValueError("Invalid airline cod {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 999):
            raise ValueError("Invalid rout number {}".format(number))
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        print(self._number)

    def airline(self):
        print(self._number[:2])

    def aircraft_model(self):
        print(self._aircraft.model())

    def _parse_seat(self, seat):
        row_number, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_number:
            raise ValueError("Invalid row number {}".format(row))
        return row, letter

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat((to_seat))
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format((to_seat)))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self.num_seats_per_row = num_seats_per_row

    def registration(self):
        print(self._registration)

    def model(self):
        print(self._model)

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self.num_seats_per_row])


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "|Name: {0}" \
             "Flight: {1}" \
             "Seat: {2}" \
             "Aircraft: {3}" \
             "|".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

# main
z = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
z.allocate_seat('12A', 'limor levi')
z.allocate_seat('12B', 'yaniv harpaz')

pp(z._seating)

# temp=z._aircraft.seating_plan()

# z.aircraft_model()

# f=Flight("SN060")
# f.number()
# f.airline()

# a=Aircraft("G-EUPT","Airbus A319",num_rows=22,num_seats_per_row=6)
# a.registration()
# a.model()
# a.seating_plan()