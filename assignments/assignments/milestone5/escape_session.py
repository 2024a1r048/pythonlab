# escape_session.py
# EscapeSession class from Milestone 3, now using the functions of escape_utils.py

from escape_utils import calculate_adjusted_time, classify_outcome, session_summary


class EscapeSession:
    venue_name = "Mystery Escape Rooms, Jammu"   # class variable

    def __init__(self, session_id, team_name, room_theme, players,
                 raw_time, hints_used, room_limit):
        self.session_id = session_id
        self.team_name = team_name
        self.room_theme = room_theme
        self.players = players
        self.raw_time = raw_time
        self.hints_used = hints_used
        self.room_limit = room_limit

    def adjusted_time(self):
        # keyword argument used for the penalty
        return calculate_adjusted_time(self.raw_time, self.hints_used,
                                       penalty_per_hint=3)

    def outcome(self):
        return classify_outcome(self.adjusted_time(), self.room_limit)

    def display_summary(self):
        print("Session ID:", self.session_id)
        print("Team Name:", self.team_name)
        print("Room Theme:", self.room_theme)
        print("Adjusted Time:", self.adjusted_time(), "minutes")
        print("Outcome:", self.outcome())

    def __str__(self):
        return session_summary(self.session_id, self.team_name, self.room_theme,
                               self.adjusted_time(), self.outcome())
