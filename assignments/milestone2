# Milestone 2: Manage Multiple Sessions using Decisions, Loops and Collections

# a) Store room limits in a dictionary (room name : time limit in minutes)
room_limits = {
    "Lost Laboratory": 60,
    "Ancient Vault": 50,
    "Space Station": 45
}

penalty_per_hint = 3
sessions = []             # list to store all valid sessions
rooms_attempted = set()   # set to store unique rooms attempted

print("Available Rooms:", list(room_limits.keys()))
print("Type DONE as team name to stop.")

# b) Repeatedly accept session details until DONE
while True:
    print()
    team_name = input("Enter team name (or DONE to finish): ").strip()
    if team_name.upper() == "DONE":
        break

    room_theme = input("Enter room theme: ").strip().title()
    players = int(input("Enter number of players: "))
    raw_time = float(input("Enter raw completion time (minutes): "))
    hints = int(input("Enter number of hints used: "))

    # c) Reject invalid sessions
    if room_theme not in room_limits:
        print("Session Rejected: Room", room_theme, "is not available.")
        continue
    if players < 2 or players > 6:
        print("Session Rejected: Players must be between 2 and 6.")
        continue
    if raw_time <= 0:
        print("Session Rejected: Raw time must be positive.")
        continue
    if hints < 0:
        print("Session Rejected: Hints cannot be negative.")
        continue

    # d) Calculate adjusted time and classify the outcome
    limit = room_limits[room_theme]
    adjusted_time = raw_time + (hints * penalty_per_hint)

    if adjusted_time <= 0.7 * limit:
        outcome = "FAST ESCAPE"
    elif adjusted_time <= limit:
        outcome = "ESCAPED"
    else:
        outcome = "TIME EXCEEDED"

    session = {
        "team": team_name.title(),
        "room": room_theme,
        "adjusted_time": adjusted_time,
        "outcome": outcome
    }
    sessions.append(session)
    rooms_attempted.add(room_theme)

    print("Session Accepted -> Adjusted Time:", adjusted_time,
          "minutes | Outcome:", outcome)

# e) Display the summary
fast_count = 0
escaped_count = 0
exceeded_count = 0

for s in sessions:
    if s["outcome"] == "FAST ESCAPE":
        fast_count += 1
    elif s["outcome"] == "ESCAPED":
        escaped_count += 1
    else:
        exceeded_count += 1

print("\n============== SESSION SUMMARY ==============")
for s in sessions:
    print(s["team"], "|", s["room"], "|", s["adjusted_time"], "min |", s["outcome"])
print("---------------------------------------------")
print("Total Valid Sessions:", len(sessions))
print("FAST ESCAPE:", fast_count)
print("ESCAPED:", escaped_count)
print("TIME EXCEEDED:", exceeded_count)

if len(sessions) > 0:
    best = sessions[0]
    for s in sessions:
        if s["adjusted_time"] < best["adjusted_time"]:
            best = s
    print("Team with Lowest Adjusted Time:", best["team"], "-",
          best["adjusted_time"], "minutes")

print("Unique Rooms Attempted:", sorted(rooms_attempted))
print("=============================================")
