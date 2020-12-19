#For conducting a random civ draft for Age of Empires II

from random import shuffle
from math import ceil

BANNER = '''
    /                                        |
O===[====================- --==/////////////[}}====*
    \                                        |
''' + " ------WELCOME TO THE WINTER 2020 AGE OF EMPIRES TOURNAMENT!-----\n\nBest of luck to all." + \
        "\nWe will now conduct the civilization draft.\n"

CIVS = ['Britons', 'Byzantines', 'Celts', 'Chinese', 'Franks', 'Goths', 'Japanese', 'Mongols', \
                 'Persians', 'Saracens', 'Teutons', 'Turks', 'Vikings', 'Aztecs', 'Huns', 'Koreans', 'Mayans', \
                 'Spanish', 'Incas', 'Indians', 'Italians', 'Magyars', 'Slavs', 'Berbers', 'Ethiopians', \
                 'Malians', 'Portuguese', 'Burmese', 'Khmer', 'Malay', 'Vietnamese', 'Bulgarians', 'Cumans', \
                 'Lithuanians', 'Tatars']

def create_civ_pool(num_players, num_picks):
    civ_pool = CIVS.copy()
    i = ceil((num_players * num_picks)/35)-1
    for _ in range(i):
        civ_pool += CIVS
    for _ in range(20):
        shuffle(civ_pool)
    return civ_pool

def complete(players, num_picks):
    total_picks = 0
    for player in players:
        total_picks += len(player)  
    if total_picks == len(players) * num_picks:
        return True
    else:
        return False

def main():
    print(BANNER)
    try:
        num_players = int(input("How many players for the draft?: "))
        if num_players < 1:
            print("You must have more than 0 players.")
            exit(0)
    except ValueError:
        print("The number of players should be an integer...swine.")
        exit(0)
    try:
        civ_picks = int(input("How many civ picks for each player?: "))
        if civ_picks < 1:
             print("You must have more than 0 picks.")
             exit(0)           
        elif civ_picks > 35:
             print("You cannot have more than 35 picks unless duplicates are allowed.")
             exit(0)        
    except ValueError:
        print("The number of picks should be an integer...swine.")
        exit(0)

    civ_pool = create_civ_pool(num_players, civ_picks)

    players = [ [] for i in range(num_players) ]

    while not complete(players, civ_picks):
        for i in range(len(players)):
            for j in range(len(civ_pool)):
                if not civ_pool[j] in players[i]:
                    players[i].append(civ_pool.pop(j))
                    break
                else:
                    pass

    print("The draft results are:\n")
    for player in players:
        player.sort()
        print("\nPlayer-----")
        for civ in player:
            print(civ)

    return 0
    
if __name__ == "__main__":
    main() 
