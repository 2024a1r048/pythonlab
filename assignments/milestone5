# main.py
# Milestone 5: File handling, exceptions and debugging (final version)

import math
from escape_session import EscapeSession
from escape_utils import outcome_counts, best_team, total_hints

FILE_NAME = "escape_sessions.txt"

room_limits = {
    "Lost Laboratory": 60,
    "Ancient Vault": 50,
    "Space Station": 45
}


# Count the saved records to create the next session ID
def next_session_id():
    try:
        file = open(FILE_NAME, "r")
        count = len(file.readlines())
        file.close()
    except FileNotFoundError:
        count = 0
    return "S" + str(101 + count)


# a) Append a session to the file using "," as separator
def save_session(session):
    # Bug fixed: earlier this used "w" mode, which deleted old records.
    # "a" (append) mode adds the new record at the end of the file.
    file = open(FILE_NAME, "a")
    record = (session.session_id + "," + session.team_name + "," +
              session.room_theme + "," + str(session.players) + "," +
              str(session.raw_time) + "," + str(session.hints_used) + "," +
              str(session.room_limit) + "," +
              str(session.adjusted_time()) + "," + session.outcome())
    file.write(record + "\n")
    file.close()


# b) and d) Read the file and convert valid records back into objects
def load_sessions():
    sessions = []
    try:
        file = open(FILE_NAME, "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error:", FILE_NAME, "not found. No sessions have been saved yet.")
        return sessions

    line_number = 0
    for line in lines:
        line_number += 1
        parts = line.strip().split(",")

        if len(parts) != 9:
            print("Warning: Malformed record on line", line_number,
                  "(expected 9 fields, found " + str(len(parts)) + ") - skipped")
            continue

        try:
            session = EscapeSession(parts[0], parts[1], parts[2], int(parts[3]),
                                    float(parts[4]), int(parts[5]), int(parts[6]))
            sessions.append(session)
        except ValueError:
            print("Warning: Invalid number in record on line", line_number, "- skipped")
    return sessions


def add_session():
    print("\n--- Add New Session ---")
    team_name = input("Enter team name: ").strip().title()
    room_theme = input("Enter room theme: ").strip().title()

    # c) Handle ValueError for numeric input
    try:
        players = int(input("Enter number of players: "))
        raw_time = float(input("Enter raw completion time (minutes): "))
        hints = int(input("Enter number of hints used: "))
    except ValueError:
        print("Invalid Input! Players and hints must be whole numbers",
              "and raw time must be a number.")
        print("Session not saved.")
        return

    if (room_theme not in room_limits or players < 2 or players > 6
            or raw_time <= 0 or hints < 0):
        print("Session Rejected: Invalid room, players, time or hints.")
        return

    session = EscapeSession(next_session_id(), team_name, room_theme, players,
                            raw_time, hints, room_limits[room_theme])
    save_session(session)
    print("Session Saved ->", session)
    print("Billing Slots Used (15 min each):", math.ceil(session.adjusted_time() / 15))


def view_sessions():
    print("\n--- Saved Sessions ---")
    sessions = load_sessions()
    for s in sessions:
        print(s)
    print("Total records loaded:", len(sessions))


def show_report():
    print("\n--- Summary Report ---")
    sessions = load_sessions()
    if len(sessions) == 0:
        print("No sessions to report.")
        return

    team, time = best_team(sessions)
    hint_list = []
    total_slots = 0
    for s in sessions:
        hint_list.append(s.hints_used)
        total_slots += math.ceil(s.adjusted_time() / 15)

    print("Total Sessions:", len(sessions))
    print("Outcome Counts:", outcome_counts(sessions))
    print("Best Team:", team, "-", time, "minutes")
    print("Total Hints:", total_hints(*hint_list))
    print("Total Billing Slots:", total_slots)


# Main menu
print("========== ESCAPE ROOM CHALLENGE TRACKER ==========")
while True:
    print("\n1. Add Session  2. View Sessions  3. Summary Report  4. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_session()
    elif choice == "2":
        view_sessions()
    elif choice == "3":
        show_report()
    elif choice == "4":
        print("Thank you! Records are saved in", FILE_NAME)
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
