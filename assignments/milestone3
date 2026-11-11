# Milestone 3: Model an Escape Session using OOP

# a) Class EscapeSession
class EscapeSession:
    # class variable (same for every session object)
    venue_name = "Mystery Escape Rooms, Jammu"

    # b) Constructor to initialize each session object
    def __init__(self, session_id, team_name, room_theme, players,
                 raw_time, hints_used, room_limit):
        self.session_id = session_id
        self.team_name = team_name
        self.room_theme = room_theme
        self.players = players
        self.raw_time = raw_time
        self.hints_used = hints_used
        self.room_limit = room_limit

    # c) Instance methods (hint penalty is 3 minutes)
    def adjusted_time(self):
        return self.raw_time + (self.hints_used * 3)

    def outcome(self):
        adj_time = self.adjusted_time()
        if adj_time <= 0.7 * self.room_limit:
            return "FAST ESCAPE"
        elif adj_time <= self.room_limit:
            return "ESCAPED"
        else:
            return "TIME EXCEEDED"

    def display_summary(self):
        print("\n---------- Session Summary ----------")
        print("Venue:", EscapeSession.venue_name)
        print("Session ID:", self.session_id)
        print("Team Name:", self.team_name)
        print("Room Theme:", self.room_theme)
        print("Players:", self.players)
        print("Raw Time:", self.raw_time, "minutes")
        print("Hints Used:", self.hints_used)
        print("Room Limit:", self.room_limit, "minutes")
        print("Adjusted Time:", self.adjusted_time(), "minutes")
        print("Outcome:", self.outcome())

    # d) __str__ returns ID, team, room, adjusted time and outcome
    def __str__(self):
        return (self.session_id + " | " + self.team_name + " | " + self.room_theme +
                " | " + str(self.adjusted_time()) + " min | " + self.outcome())


# e) Create session objects with different results
session1 = EscapeSession("S101", "Code Breakers", "Lost Laboratory", 4, 42.5, 2, 60)
session2 = EscapeSession("S102", "Puzzle Pirates", "Ancient Vault", 5, 30.0, 1, 50)
session3 = EscapeSession("S103", "Mind Benders", "Space Station", 3, 44.0, 2, 45)

session1.display_summary()
session2.display_summary()
session3.display_summary()

print("\n--- Printing objects using __str__ ---")
print(session1)
print(session2)
print(session3)
