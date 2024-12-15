import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='airline_system.db'):
        self.db_name = db_name
        self.create_tables()
    
    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create users table for authentication
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        ''')
        
        # Create Airlines table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Airlines (
            AirlineID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(100) NOT NULL,
            IATA_Code VARCHAR(3),
            ContactInfo VARCHAR(255)
        )
        ''')
        
        # Create Country table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Country (
            CountryID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(255) NOT NULL
        )
        ''')
        
        # Create City table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS City (
            CityID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(255) NOT NULL,
            CountryID INTEGER,
            FOREIGN KEY (CountryID) REFERENCES Country(CountryID)
        )
        ''')
        
        # Create Airports table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Airports (
            AirportID INTEGER PRIMARY KEY AUTOINCREMENT,
            AirportName VARCHAR(100) NOT NULL,
            CityID INTEGER,
            IATA_Code VARCHAR(3),
            FOREIGN KEY (CityID) REFERENCES City(CityID)
        )
        ''')
        
        # Create Flights table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Flights (
            FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
            AirlineID INTEGER,
            DepartureDate DATETIME,
            ArrivalDate DATETIME,
            OriginAirportID INTEGER,
            DestinationAirportID INTEGER,
            Price REAL(10,2),
            FOREIGN KEY (AirlineID) REFERENCES Airlines(AirlineID),
            FOREIGN KEY (OriginAirportID) REFERENCES Airports(AirportID),
            FOREIGN KEY (DestinationAirportID) REFERENCES Airports(AirportID)
        )
        ''')
        
        # Create Passengers table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Passengers (
            PassengerID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName VARCHAR(50) NOT NULL,
            LastName VARCHAR(50) NOT NULL,
            Email VARCHAR(100),
            PhoneNumber VARCHAR(15)
        )
        ''')
        
        # Create Tickets table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tickets (
            TicketID INTEGER PRIMARY KEY AUTOINCREMENT,
            SeatNumber VARCHAR(10),
            Price REAL(10,2),
            Status VARCHAR(20),
            PassengerID INTEGER,
            BookingDate DATETIME,
            FlightID INTEGER,
            FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID),
            FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def register_user(self, login, email, password):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (login, email, password) VALUES (?, ?, ?)',
                         (login, email, password))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def check_user_exists(self, login, password):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE login = ? AND password = ?',
                      (login, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    
    def check_login_exists(self, login):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    
    def check_email_exists(self, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        return user is not None
        
    def get_tickets(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Tickets')
        tickets = cursor.fetchall()
        conn.close()
        return tickets

    def get_flights_by_airline(self, airline_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE AirlineID = ?', (airline_id,))
        flights = cursor.fetchall()
        conn.close()
        return flights
    
    def get_flights_by_date(self, date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE DepartureDate = ? OR ArrivalDate = ?', (date, date))
        flights = cursor.fetchall()
        conn.close()
        return flights

    def get_flights_by_city(self, city_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE OriginAirportID = ? OR DestinationAirportID = ?', (city_id, city_id))
        flights = cursor.fetchall()
        conn.close()
        return flights

    def get_flights_by_country(self, country_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE OriginAirportID = ? OR DestinationAirportID = ?', (country_id, country_id))
        flights = cursor.fetchall()
        conn.close()
        return flights

    def get_flights_by_airline_and_city(self, airline_id, city_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE AirlineID = ? AND (OriginAirportID = ? OR DestinationAirportID = ?)', (airline_id, city_id, city_id))
        flights = cursor.fetchall()
        conn.close()
        return flights

    def get_flights_by_airline_and_country(self, airline_id, country_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE AirlineID = ? AND (OriginAirportID = ? OR DestinationAirportID = ?)', (airline_id, country_id, country_id))
        flights = cursor.fetchall()
        conn.close()
        return flights
    
    def get_flights_by_city_and_date(self, city_id, date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Flights WHERE OriginAirportID = ? OR DestinationAirportID = ? AND (DepartureDate = ? OR ArrivalDate = ?)', (city_id, city_id, date, date))
        flights = cursor.fetchall()
        conn.close()
        return flights

    