class Airport:
    def __init__(self, name,departure_city,departure_time,arrival_city,weather,departure_day,arrival_day,arrival_time):
        self.name = name
        self.ticket_sales = 0
        self.departure_city = departure_city
        self.departure_time = departure_time
        self.arrival_city = arrival_city
        self.arrival_time = arrival_time
        self.weather = weather
        self.departure_day = departure_day
        self.arrival_day = arrival_day

    def register_ticket(self, num_tickets):
        self.ticket_sales += num_tickets

    def set_departure_time(self, time):
        self.departure_time = time

    def set_departure_city(self, city):
        self.departure_city = city

    def set_arrival_time(self, time):
        self.arrival_time = time

    def set_arrival_city(self, city):
        self.arrival_city = city

    def set_weather(self, weather):
        self.weather = weather

    def set_departure_day(self, day):
        self.departure_day = day

    def set_arrival_day(self, day):
        self.arrival_day = day


name = input("Aeroport nomini kiriting: ")
ticket_count = int(input("Bilet sotib olishlar sonini kiriting: "))
departure_time = input("Uchish vaqti ni kiriting: ")
departure_city = input("Uchish shahri ni kiriting: ")
arrival_time = input("Qunish vaqti ni kiriting: ")
arrival_city = input("Qunish shahri ni kiriting: ")
weather = input("Ob-havo ni kiriting: ")
departure_day = input("Uchish kunini kiriting: ")
arrival_day = input("Qunish kunini kiriting: ")

aeroport = Airport(name)
aeroport.register_ticket(ticket_count)
aeroport.set_departure_time(departure_time)
aeroport.set_departure_city(departure_city)
aeroport.set_arrival_time(arrival_time)
aeroport.set_arrival_city(arrival_city)
aeroport.set_weather(weather)
aeroport.set_departure_day(departure_day)
aeroport.set_arrival_day(arrival_day)


print("Aeroport nomi:", aeroport.name)
print("Bilet sotib olishlar soni:", aeroport.ticket_sales)
print("Uchish vaqti:", aeroport.departure_time)
print("Uchish shahri:", aeroport.departure_city)
print("Qunish vaqti:", aeroport.arrival_time)
print("Qunish shahri:", aeroport.arrival_city)
print("Ob-havo:", aeroport.weather)
print("Uchish kun:", aeroport.departure_day)
print("Qunish kun:", aeroport.arrival_day)
