#Text based adventure game. 
"""
The objective is to find the treasure by making the right choices and overcoming obstacles, 
successfully navigating the adventure. If the player makes poor decisions, they may lose 
their way or fail the quest.
"""

# Helper function to check for quit command
def check_quit(user_input):
    if user_input.lower().strip() == 'q':
        print("Thanks for playing! Goodbye!")
        exit()
    return user_input

#Create a function start_game()to display the game introduction, ask the player for their name and provide an initial choice (explore a forest or enter a cave). 
def start_game():
    print("Welcome to the Adventure Game!")
    name = input("Please enter your name (or 'q' to quit): ")
    check_quit(name)
    print(f"Hello, {name}! Your adventure begins now.")
    print("You find yourself at a crossroads. Do you want to explore the forest or enter the cave?")
    choice = check_quit(input("Type 'forest' to explore the forest or 'cave' to enter the cave (or 'q' to quit): ")).lower().strip()
    
    if 'forest' in choice:
        explore_forest()
    elif 'cave' in choice:
        enter_cave()
    else:
        print("Invalid choice. Please try again.")
        start_game()

# Create function forest_path() that describes the forest scenario, Provide the player with choices (follow a river or climb a tree)Use an if-else structure to handle player choices
def explore_forest():
    print("You enter the forest and see a river and a tall tree nearby.")
    choice = check_quit(input("Do you want to 'cross the river' or 'climb the tree' (or 'q' to quit)? ")).lower().strip()
    if 'cross' in choice and 'river' in choice:
        print("How will you cross the deep river!")
        river_crossing()

    elif 'climb' in choice and 'tree' in choice:
        print("You climb the tree and see a beautiful view of the forest.")
        print("Suddenly, a branch breaks under your weight!")
        choice = check_quit(input("Do you want to 'grab another branch' or 'jump down' (or 'q' to quit)? ")).lower().strip()
        if 'grab' in choice:
            print("You manage to grab another branch and steady yourself.")
            print("You spot a hidden path. Will it lead to the treasure or danger?")
            choice = check_quit(input("Do you want to 'follow the hidden path' or 'go back to the crossroads' (or 'q' to quit)? ")).lower().strip()
            if 'follow' in choice and 'path' in choice:
                hidden_path()
            elif 'go back' in choice or 'crossroads' in choice:
                start_game()
        elif 'jump' in choice:
            print("You jump down but land badly and twist your ankle. You limp back to the crossroads.")
            start_game()
        else:
            print("Invalid choice. Please try again.")
            explore_forest()
    else:
        print("Invalid choice. Please try again.")
        explore_forest()



def enter_cave():
    print("You enter a dark cave. You hear strange sounds.")
    choice = check_quit(input("Do you want to 'explore deeper' or 'go back' (or 'q' to quit)? ")).lower().strip()
    if 'explore' in choice and 'deeper' in choice:
        cave_exploration()       
    elif 'go back' in choice:
        print("You decide to go back to the crossroads.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        enter_cave()

#Create additional functions for the river crossing, hidden path, and cave exploration scenarios to further develop the game and provide more choices for the player.
def river_crossing():
    print("You attempt to cross the river. The current is strong.")
    choice = check_quit(input("Do you want to 'swim across' or 'look for a raft' (or 'q' to quit)? ")).lower().strip()
    if 'swim' in choice:
        print("You manage to swim across but lose some supplies in the process.")
        print("The current is strong and you're getting tired...")
        choice = check_quit(input("Do you want to 'keep swimming' or 'turn back' (or 'q' to quit)? ")).lower().strip()
        if 'keep' in choice or 'swim' in choice:
            print("You continue your search and find a hidden cave.")
            choice = check_quit(input("Do you want to 'enter the cave' or 'go back to the crossroads' (or 'q' to quit)? ")).lower().strip()
            if 'enter' in choice and 'cave' in choice:
                print("Congratulations! You found the treasure and won the game!")
            elif 'go back' in choice or 'crossroads' in choice:
                start_game()
            else:
                print("Invalid choice. Please try again.")
                river_crossing()
        elif 'turn' in choice or 'back' in choice:
            print("You turn back and swim to shore, exhausted. You decide to head back to the crossroads.")
            start_game()
        else:
            print("Invalid choice. Please try again.")
            river_crossing()
    elif 'raft' in choice:
        print("You find a rickety raft and carefully cross the river.")
        print("Suddenly, the raft starts to leak!")
        choice = check_quit(input("Do you want to 'paddle faster' or 'fix the leak' (or 'q' to quit)? ")).lower().strip()
        if 'paddle' in choice:
            print("You paddle fast and make it across, soaking wet but alive!")
            choice = check_quit(input("Do you want to 'continue looking for treasure' or 'go back' (or 'q' to quit)? ")).lower().strip()
            if 'continue' in choice:
                print("You continued your search and find a hidden cave.")
                choice = check_quit(input("Do you want to 'enter the cave' or 'go back to the crossroads' (or 'q' to quit)? ")).lower().strip()
                if 'enter' in choice and 'cave' in choice:
                    print("Congratulations! You found the treasure and won the game!")
                elif 'go back' in choice or 'crossroads' in choice:
                    start_game()
                else:
                    print("Invalid choice. Please try again.")
                    river_crossing()
            elif 'go back' in choice:
                start_game()
            else:
                print("Invalid choice. Please try again.")
                river_crossing()
        elif 'fix' in choice:
            print("You try to fix the leak but the raft sinks. You barely make it back to shore.")
            print("Exhausted, you return to the crossroads.")
            start_game()
        else:
            print("Invalid choice. Please try again.")
            river_crossing()

def hidden_path():
    print("You follow the hidden path and encounter a mysterious old man.")
    choice = check_quit(input("Do you want to 'talk to the old man' or 'ignore him and continue' (or 'q' to quit)? ")).lower().strip()
    if 'talk' in choice:
        print("The old man gives you a clue about the treasure's location.")
        print("Congratulations! You found the treasure and won the game!")
    elif 'ignore' in choice:
        print("You ignore the old man and continue down the path, but you get lost in the forest.")
        # Handle getting lost scenario here 
        lost_in_forest()
    else:
        print("Invalid choice. Please try again.")
        hidden_path()           

def lost_in_forest():
    print("You wander aimlessly in the forest and eventually find yourself back at the crossroads.")
    start_game()

def cave_exploration():
    print("You explore deeper into the cave and find a hidden passage.")
    print("The cave gets darker and you hear creaking sounds...")
    choice = check_quit(input("Do you want to 'continue cautiously' or 'turn back immediately' (or 'q' to quit)? ")).lower().strip()
    if 'continue' in choice:
        print("You carefully explore deeper and find a hidden chamber with a treasure chest!")
        print("Congratulations! You found the treasure and won the game!")
    elif 'turn' in choice:
        print("You wisely turn back. A moment later, a large section of the cave collapses where you just were!")
        print("You escape back to the crossroads, shaken but alive.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        enter_cave()

# Start the game by calling the start_game() function.
#start_game()

