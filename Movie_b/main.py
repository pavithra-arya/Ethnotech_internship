from booking.booking_system import BookingSystem


def main():
    system = BookingSystem()

    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. Book Ticket")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.book_ticket()
        elif choice == "2":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
