class Flight:

    def __init__(self, pid, start_time, priority):
        self.pid = pid
        self.start_time = start_time
        self.priority = priority

    def __repr__(self):
        return f"Flight({self.pid}, {self.start_time}, {self.priority})"


def sort_flights(flights, sort_by):
    if sort_by == 1:
        flights.sort(key=lambda flight: flight.pid)
    elif sort_by == 2:
        flights.sort(key=lambda flight: flight.start_time)
    elif sort_by == 3:
        flights.sort(key=lambda flight: flight.priority)
    else:
        raise ValueError("Invalid sort option")


if __name__ == "__main__":

    flights = [
        Flight("P1", 100, "MID"),
        Flight("P23", 234, "MID"),
        Flight("P93", 189, "High"),
        Flight("P42", 9, "High"),
        Flight("P9", 7, "High"),
        Flight("P87", 23, "Low"),
    ]

    sort_by = int(input("Enter the sorting option: "))
    sort_flights(flights, sort_by)

    print("Sorted flights:")
    for flight in flights:
        print(flight)
