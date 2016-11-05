"""Model for aircraft flights"""


class Flight:
    """A flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        letter, row = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format((seat)))

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        return letter, row


class Aircraft:
    """Class AirCraft"""
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows + 1),
                "ABCDEFGHIJK"[:self._num_seats_per_row])



# f = Flight("BA758", Aircraft("G_EUPT", "AirBus A319", num_rows=22, num_seats_per_row=6))