class Volunteer:
    def __init__(self, volunteer_id, name, email, phone):
        self.volunteer_id = volunteer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.assignments = []

    def update_details(self, name=None, email=None, phone=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def assign_to_event(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments


class Event:
    def __init__(self, event_id, name, date, location):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments


class Organization:
    def __init__(self, name):
        self.name = name
        self.volunteers = []
        self.events = []

    def add_volunteer(self, volunteer):
        self.volunteers.append(volunteer)

    def remove_volunteer(self, volunteer_id):
        self.volunteers = [v for v in self.volunteers if v.volunteer_id != volunteer_id]

    def add_event(self, event):
        self.events.append(event)

    def get_volunteers(self):
        return self.volunteers

    def get_events(self):
        return self.events

class Assignment:
    def __init__(self, assignment_id, volunteer, event, role):
        self.assignment_id = assignment_id
        self.volunteer = volunteer
        self.event = event
        self.role = role

    def get_details(self):
        return {
            "assignment_id": self.assignment_id,
            "volunteer_name": self.volunteer.name,
            "event_name": self.event.name,
            "role": self.role
        }


org = Organization("Helping Hands")


volunteer1 = Volunteer(1, "John Doe", "john@example.com", "123-456-7890")
volunteer2 = Volunteer(2, "Jane Smith", "jane@example.com", "098-765-4321")

org.add_volunteer(volunteer1)
org.add_volunteer(volunteer2)


event1 = Event(1, "Charity Run", "2024-07-15", "Central Park")


org.add_event(event1)

assignment1 = Assignment(1, volunteer1, event1, "Coordinator")
assignment2 = Assignment(2, volunteer2, event1, "Participant")

volunteer1.assign_to_event(assignment1)
volunteer2.assign_to_event(assignment2)
event1.add_assignment(assignment1)
event1.add_assignment(assignment2)

for assignment in event1.get_assignments():
    print(assignment.get_details())
