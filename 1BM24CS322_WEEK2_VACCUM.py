# Vacuum Cleaner Agent

def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


def goal_based_agent(location, room_a, room_b):
    actions = []

    while room_a == "Dirty" or room_b == "Dirty":

        if location == "A":
            if room_a == "Dirty":
                actions.append("Suck")
                room_a = "Clean"
            else:
                actions.append("Move Right")
                location = "B"

        else: 
            if room_b == "Dirty":
                actions.append("Suck")
                room_b = "Clean"
            else:
                actions.append("Move Left")
                location = "A"

    actions.append("Goal Achieved")
    return actions


# Simple Reflex Agent

print("----- SIMPLE REFLEX AGENT -----")

location = input("Enter vacuum location (A/B): ")
status = input("Enter status (Clean/Dirty): ")

action = simple_reflex_agent(location, status)

print("Action:", action)


# Goal Based Agent

print("\n----- GOAL BASED AGENT -----")

location = input("Enter vacuum location (A/B): ")
room_a = input("Enter status of Room A (Clean/Dirty): ")
room_b = input("Enter status of Room B (Clean/Dirty): ")

actions = goal_based_agent(location, room_a, room_b)

print("\nActions:")
for action in actions:
    print(action)
