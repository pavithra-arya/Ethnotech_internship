from booking.movie import Movie
from booking.theatre import Theatre


class BookingSystem:
    def __init__(self):
        self.movies = [
            Movie("Leo", 150),
            Movie("Jailer", 180),
            Movie("KGF", 200)
        ]
        self.theatre = Theatre(10)

    def display_movies(self):
        print("\nAvailable Movies:")
        for index, movie in enumerate(self.movies, start=1):
            print(f"{index}. {movie}")

    def display_seats(self):
        print("\nAvailable Seats:")
        for seat in self.theatre:
            print(seat, end=" ")
        print()

    def book_ticket(self):
        self.display_movies()
        choice = int(input("\nSelect movie number: ")) - 1

        if 0 <= choice < len(self.movies):
            selected_movie = self.movies[choice]
            print(f"\nYou selected: {selected_movie.name}")

            self.display_seats()
            seat_choice = input("\nEnter seat number to book: ")

            if self.theatre.book_seat(seat_choice):
                print("\n✅ Booking Successful!")
                print(f"Movie: {selected_movie.name}")
                print(f"Seat: {seat_choice}")
                print(f"Total Amount: ₹{selected_movie.price}")
            else:
                print("\n❌ Seat not available!")
        else:
            print("\nInvalid movie selection!")
