class Event:
    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        self.participant_count += 1  # Increase participant count by 1

    def get_participant_count(self):
        return self.participant_count  # Retrieve the current participant count
        