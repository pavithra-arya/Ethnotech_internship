class SeatIterator:
    def __init__(self, seats):
        self._seats = seats
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._seats):
            seat = self._seats[self._index]
            self._index += 1
            return seat
        else:
            raise StopIteration


class Theatre:
    def __init__(self, total_seats):
        self.available_seats = [f"S{i}" for i in range(1, total_seats + 1)]

    def __iter__(self):
        return SeatIterator(self.available_seats)

    def book_seat(self, seat):
        if seat in self.available_seats:
            self.available_seats.remove(seat)
            return True
        return False
