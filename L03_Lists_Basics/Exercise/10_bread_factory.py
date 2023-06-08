events = input().split("|")
total_energy = 100
total_coins = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:  # order can be completed
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_is_open = False
            break
if factory_is_open:  # if factory is open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {type_of_event}.")

# Description #
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. Each
# event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-
# {number}")
# • If the event is "rest":© SoftUni – about.softuni.bg. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 8 of 9
# o You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy
# (100). Print: "You gained {gained_energy} energy.".
# o After that, print your current energy: "Current energy: {current_energy}.".
# • If the event is "order":
# o You've earned some coins (the number in the second part).
# o Each time you get an order, your energy decreases by 30 points.
# ▪ If you have the energy to complete the order, print: "You earned {earned} coins.".
# ▪ Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# • In any other case, you have an ingredient you should buy. The second part of the event contains the coins
# you should spend.
# o If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# o Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events throughout the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"
# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format:
# "{event/ingredient}-{number}"
# Output
# Print the corresponding messages described above.
