# Task 1.  Begin with the End in Mind

# Lists 

def players():
    # List of soccer players
    players_defense = ["Ramsdale", "Gabriel", "Zinchenko", "Saliba", "White"]

    # Add a defender
    players_defense.append("Tomiyasu")

    # Sort the list
    players_defense.sort()

    # Return the list
    return players_defense

print(players())


# Sets 
def epl():
    # Set of teams 
    teams = {"Arsenal", "Chelsea", "Liverpool", "Manchester City"}
    # Add a team
    teams.add("Newcastle")

    # Remove a team
    teams.remove("Chelsea")

    # Check if a team is in the set
    print("Newcastle" in teams)

epl()


# tuple 

def soccer_players():
    # Attacking soccer players
    players_attack = ("Saka", "Martinelli", "Trossard", "Viera")

    # Add a forward
    players_attack = players_attack + ("Henry",)

    # Sort the tuple
    players_attack = tuple(sorted(players_attack))

    # Return the tuple
    return players_attack

print(soccer_players())

 