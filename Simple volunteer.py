class Volunteer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.assignments = []

    def add_assignment(self, event):
        self.assignments.append(event)

    def remove_assignment(self, event):
        self.assignments.remove(event)

class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.volunteers = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def remove_volunteer(self, volunteer):
        self.volunteers.remove(volunteer)

class Organization:
    def __init__(self, name):
        self.name = name
        self.events = []
        self.volunteers = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events.remove(event)

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def remove_volunteer(self, volunteer):
        self.volunteers.remove(volunteer)

class Assignment:
    def __init__(self, volunteer, event):
        self.volunteer = volunteer
        self.event = event

    def __str__(self):
        return f"{self.volunteer.name} is assigned to {self.event.name}"


org = Organization("Volunteer Org")

event1 = Event("Charity Run", "2024-07-01", "Central Park")
event2 = Event("Food Drive", "2024-07-15", "Community Center")

org.add_event(event1)
org.add_event(event2)

volunteer1 = Volunteer(input(), "johndoe@example.com", "1234567890")
volunteer2 = Volunteer(input(), "janesmith@example.com", "0987654321")

org.add_volunteer(volunteer1)
org.add_volunteer(volunteer2)

assignment1 = Assignment(volunteer1, event1)
assignment2 = Assignment(volunteer2, event2)

volunteer1.add_assignment(event1)
event1.add_volunteer(volunteer1)

volunteer2.add_assignment(event2)
event2.add_volunteer(volunteer2)

print(assignment1)  # Output: John Doe is assigned to Charity Run
print(assignment2)  # Output: Jane Smith is assigned to Food Drive
