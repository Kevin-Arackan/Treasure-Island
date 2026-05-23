print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('''
    Welcome to Treasure Island!
    Your mission is to find the treasure.''')


# Crossroads

direction = input('''
    You  encounter a crossroad. There are two paths.
    The left one will take you to a lake with a small island.
    The right one will take you to a long desert.
    Which one will you pick?
    (Type 'left' to go left, 'right' to go right): ''')

direction = direction.lower()

if direction == "right":
    print('''
    You died of thirst in the desert.
    Game Over.
    ''')
elif direction != "left":
    print('''
    You got eaten by a leopard.
    Game Over.
    ''')
else:
    # Lake

    action = input('''
    You arrive at the lake.
    There is an island in the middle of the lake.
    You can wait for a boat or swim across.
    What do you do?
    (Type 'wait' to wait for a boat,
    or 'swim' to swim across): ''')

    action = action.lower()

    if action == "swim":
        print('''
    You got murdered by hippos.
    Game Over.
        ''')
    elif action != "wait":
        print('''
    You got lost in the lake and drowned.
    Game Over.
        ''')
    else:
        # Boat
        boat = input('''
    You encounter a small boat with a few armed individuals.
    Do you want to board the boat?
    (Type 'yes' to board the boat, or 'no' to stay on the island): ''')

        boat = boat.lower()

        if boat == "yes":
            print('''
    You got kidnapped by pirates.
    Game Over.
            ''')
        elif boat != "no":
            print('''
    The armed pirates laughed.
    They shot you in the head.
    Game Over.
            ''')
        else:
            # Ship
            ship = input('''
    The armed pirates leave you alone.
    You see a ship coming to you.
    Do you want to board the ship?
    (Type 'yes' to board the ship,
    or 'no' to stay on the island): ''')
            
            ship = ship.lower()

            if ship != "yes":
                print('''
    You got eaten by crocodiles.
    Game Over.
                ''')
            else:
                # Treasure
                treasure = input('''
    You board the ship and it takes you to the island.
    Pirates come to shoot at you.
    The island contains three caves:
    A black one, a yellow one and a wide one.
    Which cave do you enter?
    (Type 'black' to enter the black cave,
    'yellow' to enter the yellow cave,
    or 'wide' to enter the wide cave): ''')
                
                treasure = treasure.lower()

                if treasure == "black":
                    print('''
    You fell into a pit.
    Game Over.
                    ''')
                elif treasure == "wide":
                    print('''
    You entered the Lion's den and got eaten.
    Game Over.
                    ''')
                elif treasure != "yellow":
                    print('''
    You got shot by the pirates.
    Game Over.
                    ''')
                else:
                    print('''
    You found the treasure!
    You Win!
                    ''')