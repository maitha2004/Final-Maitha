#UML code

class Employee:
  def __init__(self, name, age, passport_details):
    self.name = name
    self.age = age
    self.passport_details = passport_details

  def get_info(self):
    return f"Employee: {self.name}, Age: {self.age}"

class Supplier:
  def __init__(self, name, contact_details):
    self.name = name
    self.contact_details = contact_details

  def get_info(self):
    return f"Supplier: {self.name}, Contact: {self.contact_details}"

class Venue:
  def __init__(self, name, max_guests):
    self.name = name
    self.max_guests = max_guests

  def get_info(self):
    return f"Venue: {self.name}, Max Guests: {self.max_guests}"

class Event:
  def __init__(self, name, event_type, contact_details):
    self.name = name
    self.event_type = event_type
    self.contact_details = contact_details
    self.venue = None  # Initially no venue assigned
    self.guests = []  # List to store guest objects

  def assign_venue(self, venue):
    self.venue = venue

  def register_guest(self, guest):
    self.guests.append(guest)

  def get_info(self):
    venue_info = "Not assigned" if not self.venue else self.venue.get_info()
    return f"Event: {self.name}, Type: {self.event_type}, Contact: {self.contact_details}, Venue: {venue_info}"

class Guest:
  def __init__(self, name, address, contact_details):
    self.name = name
    self.address = address
    self.contact_details = contact_details

  def get_info(self):
    return f"Guest: {self.name}, Address: {self.address}, Contact: {self.contact_details}"

# Test case
employee1 = Employee("Khalid Nasser", 30, "12345678")  # Updated employee name
supplier1 = Supplier("ACME Inc.", "info@acme.com")
venue1 = Venue("Grand Hall", 500)
event1 = Event("Company Conference", "Business", "events@mycompany.com")

event1.assign_venue(venue1)
guest1 = Guest("Jane Smith", "123 Main St", "jane.smith@email.com")
event1.register_guest(guest1)

print(employee1.get_info())
print(supplier1.get_info())
print(venue1.get_info())
print(event1.get_info())
print(guest1.get_info())
