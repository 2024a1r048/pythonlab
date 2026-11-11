# escape_utils.py
# Milestone 4: Reusable functions for the Escape Room Challenge Tracker

# a) Adjusted time calculation
# c) penalty_per_hint is a default/keyword parameter
def calculate_adjusted_time(raw_time, hints_used, penalty_per_hint=3):
    return raw_time + (hints_used * penalty_per_hint)


# a) Outcome classification
def classify_outcome(adjusted_time, room_limit):
    if adjusted_time <= 0.7 * room_limit:
        return "FAST ESCAPE"
    elif adjusted_time <= room_limit:
        return "ESCAPED"
    else:
        return "TIME EXCEEDED"


# a) Session summary generation
def session_summary(session_id, team_name, room_theme, adjusted_time, outcome):
    return (session_id + " | " + team_name + " | " + room_theme + " | " +
            str(adjusted_time) + " min | " + outcome)


# b) Functions that receive the whole session collection
def outcome_counts(sessions):
    counts = {"FAST ESCAPE": 0, "ESCAPED": 0, "TIME EXCEEDED": 0}
    for s in sessions:
        counts[s.outcome()] += 1
    return counts


def best_team(sessions):
    best = sessions[0]
    for s in sessions:
        if s.adjusted_time() < best.adjusted_time():
            best = s
    return best.team_name, best.adjusted_time()


# d) Variable number of arguments
def total_hints(*hint_counts):
    total = 0
    for h in hint_counts:
        total = total + h
    return total
