# main.py
# Milestone 4: Organize the application using functions and modules

import math
from escape_session import EscapeSession
from escape_utils import outcome_counts, best_team, total_hints

room_limits = {
    "Lost Laboratory": 60,
    "Ancient Vault": 50,
    "Space Station": 45
}

sessions = []
session_number = 101

print("========== ESCAPE ROOM CHALLENGE TRACKER ==========")
print("Available Rooms:", list(room_limits.keys()))

while True:
    print()
    team_name = input("Enter team name (or DONE to finish): ").strip()
    if team_name.upper() == "DONE":
        break

    room_theme = input("Enter room theme: ").strip().title()
    players = int(input("Enter number of players: "))
    raw_time = float(input("Enter raw completion time (minutes): "))
    hints = int(input("Enter number of hints used: "))

    if (room_theme not in room_limits or players < 2 or players > 6
            or raw_time <= 0 or hints < 0):
        print("Session Rejected: Invalid room, players, time or hints.")
        continue

    session_id = "S" + str(session_number)
    session_number += 1

    session = EscapeSession(session_id, team_name.title(), room_theme, players,
                            raw_time, hints, room_limits[room_theme])
    sessions.append(session)

    # e) Billing slots of 15 minutes using math.ceil
    slots = math.ceil(session.adjusted_time() / 15)
    print("Session Saved ->", session)
    print("Billing Slots Used (15 min each):", slots)

# Final report using the imported functions
if len(sessions) > 0:
    print("\n================ SESSION REPORT ================")
    for s in sessions:
        print(s)

    counts = outcome_counts(sessions)      # passing the session list to a function
    team, time = best_team(sessions)

    print("-----------------------------------------------")
    print("Total Sessions:", len(sessions))
    print("Outcome Counts:", counts)
    print("Best Team:", team, "-", time, "minutes")

    # d) total_hints() with a variable number of arguments
    hint_list = []
    for s in sessions:
        hint_list.append(s.hints_used)

    print("Hints in each session:", hint_list)
    print("Total Hints (total_hints(*hint_list)):", total_hints(*hint_list))
    print("total_hints(2, 1, 3) =", total_hints(2, 1, 3))

    total_slots = 0
    for s in sessions:
        total_slots += math.ceil(s.adjusted_time() / 15)
    print("Total Billing Slots:", total_slots)
    print("================================================")
else:
    print("No sessions recorded.")
