# Represents a flight with a flight number, departure airport, arrival airport, date, and time.
class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, date, time):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.date = date
        self.time = time

    def get_flight_number(self):
        return self.flight_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_departure_airport(self):
        return self.departure_airport

    def set_departure_airport(self, departure_airport):
        self.departure_airport = departure_airport

    def get_arrival_airport(self):
        return self.arrival_airport

    def set_arrival_airport(self, arrival_airport):
        self.arrival_airport = arrival_airport

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

# Represents a domestic flight which is a type of flight with an aircraft type and an operation airline.
class DomesticFlight(Flight):
    def __init__(self, aircraft_type, operation_airline, flight_number, departure_airport, arrival_airport, date, time):
        super().__init__(flight_number, departure_airport, arrival_airport, date, time)
        self.aircraft_type = aircraft_type
        self.operation_airline = operation_airline

    def get_aircraft_type(self):
        return self.aircraft_type

    def set_aircraft_type(self, aircraft_type):
        self.aircraft_type = aircraft_type

    def get_operation_airline(self):
        return self.operation_airline

    def set_operation_airline(self, operation_airline):
        self.operation_airline = operation_airline

# Represents a passenger with a name, email, and password.
class Passenger:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

# Represents a seat with a seat number and class type.
class Seat:
    def __init__(self, seat_number, class_type):
        self.seat_number = seat_number
        self.class_type = class_type

    def get_seat_number(self):
        return self.seat_number

    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def get_class_type(self):
        return self.class_type

    def set_class_type(self, class_type):
        self.class_type = class_type

# Represents a boarding pass with a passenger, flight, seat, ticket number, gate, and boarding time.
class BoardingPass:
    def __init__(self, passenger, flight, seat, ticket_number, gate, boarding_time):
        self.passenger = passenger  # Passenger object
        self.flight = flight  # Flight object
        self.seat = seat  # Seat object
        self.ticket_number = ticket_number
        self.gate = gate
        self.boarding_time = boarding_time

    def get_passenger(self):
        return self.passenger

    def set_passenger(self, passenger):
        self.passenger = passenger

    def get_flight(self):
        return self.flight

    def set_flight(self, flight):
        self.flight = flight

    def get_seat(self):
        return self.seat

    def set_seat(self, seat):
        self.seat = seat

    def get_ticket_number(self):
        return self.ticket_number

    def set_ticket_number(self, ticket_number):
        self.ticket_number = ticket_number

    def get_gate(self):
        return self.gate

    def set_gate(self, gate):
        self.gate = gate

    def get_boarding_time(self):
        return self.boarding_time

    def set_boarding_time(self, boarding_time):
        self.boarding_time = boarding_time



# Create flight object
flight = Flight(flight_number='NA4321', departure_airport='Chicago', arrival_airport='New York', date='2020, 12, 6' ,time='11, 40')

# Create seat object
seat = Seat(seat_number='09A', class_type='First Class')

# Create passenger object
passenger = Passenger(name='James Smith', email='james.smith@example.com', password='secret')

# Create boarding pass object
boarding_pass = BoardingPass(passenger=passenger, flight=flight, seat=seat, ticket_number='5A6BCD78', gate='03', boarding_time='2020, 12, 6')

# Print flight details
print("Flight Details:")
print("Flight Number:", flight.get_flight_number())
print("Departure Airport:", flight.get_departure_airport())
print("Arrival Airport:", flight.get_arrival_airport())
print("Date:", flight.get_date())
print("Time:", flight.get_time())

# Print seat details
print("\nSeat Details:")
print("Seat Number:", seat.get_seat_number())
print("Class Type:", seat.get_class_type())

# Print passenger details
print("\nPassenger Details:")
print("Name:", passenger.get_name())
print("Email:", passenger.get_email())
print("Password:", passenger.get_password())

# Print boarding pass details
print("\nBoarding Pass Details:")
print("Ticket Number:", boarding_pass.get_ticket_number())
print("Gate:", boarding_pass.get_gate())
print("Boarding Time:", boarding_pass.get_boarding_time())

# Additional details about passenger, flight, and seat in boarding pass
print("\nAdditional Details from Boarding Pass:")
print("Passenger Name:", boarding_pass.get_passenger().get_name())
print("Flight Number:", boarding_pass.get_flight().get_flight_number())
print("Seat Number:", boarding_pass.get_seat().get_seat_number())