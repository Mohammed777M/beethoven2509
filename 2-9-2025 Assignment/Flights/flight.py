class Flight:
    def __init__(self, flight_id, airline, source, destination, departure_time, arrival_time, price, seats):
        self.flight_id = flight_id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.seats = seats

    def __str__(self):
        return (f"[Flight ID={self.flight_id}, Airline={self.airline}, Source={self.source}, "
                f"Destination={self.destination}, Departure={self.departure_time}, Arrival={self.arrival_time}, "
                f"Price={self.price}, Seats={self.seats}]")

    def __repr__(self):
        return self.__str__()
    
Flight_indigo=Flight(1001,'indigo','Bangalore','Chennai','1pm','4pm',100,200)

print(Flight_indigo)