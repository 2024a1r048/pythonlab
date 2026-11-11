# Milestone 1: Record One Escape Room Session

# a) Accept session details
team_name = input("Enter team name: ")
room_theme = input("Enter room theme: ")
players = int(input("Enter number of players: "))
raw_time = float(input("Enter raw completion time (minutes): "))
hints = int(input("Enter number of hints used: "))
penalty_per_hint = float(input("Enter penalty minutes per hint: "))

# b) Display data types
print("\n--- Data Types ---")
print("Players data type:", type(players))
print("Raw time data type:", type(raw_time))

# c) Calculate penalty and adjusted time
total_penalty = hints * penalty_per_hint
adjusted_time = raw_time + total_penalty

# d) Format team and room names
formatted_team = team_name.strip().title()
formatted_room = room_theme.strip().title()

# Generate session code using first three characters
session_code = (
    formatted_team[:3].upper() + "-" +
    formatted_room[:3].upper()
)

# e) Display session details
print("\n========== ESCAPE ROOM SESSION REPORT ==========")
print("Team Name:", formatted_team)
print("Room Theme:", formatted_room)
print("Number of Players:", players)
print("Raw Completion Time:", raw_time, "minutes")
print("Hints Used:", hints)
print("Penalty Per Hint:", penalty_per_hint, "minutes")
print("Total Hint Penalty:", total_penalty, "minutes")
print("Adjusted Completion Time:", adjusted_time, "minutes")
print("Session Code:", session_code)
print("================================================")
