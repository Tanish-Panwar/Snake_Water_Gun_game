# Game-Development: Snake-Water-Gun.....

# we need to create a program of snake water and gun game .....
import random
swg = ["Snake", "Water", "Gun"]
print("(S)for Snake, (W)for Water, (G)for Gun")
win = 0
lose = 0
draw = 0
i = 0
while i<10:
    i+=1
    comp = random.choice(swg)
    player = input("Computer has choosen What will you choose: \n")
    if "S" in player and "Snake" in comp:
        print(f"Draw -Player-{player} computer-{comp}")
        draw+=1
    if "S" in player and "Gun" in comp:
        print(f"Lose - Player-{player} computer-{comp}")
        lose+=1
    if "S" in player and "Water" in comp:
        print(f"Win - Player-{player} computer-{comp}")
        win+=1

    elif "W" in player and "Water" in comp:
        print(f"Draw -Player-{player} computer-{comp}")
        draw+=1
    if "W" in player and "Snake" in comp:
        print(f"Lose - Player-{player} computer-{comp}")
        lose+=1
    if "W" in player and "Gun" in comp:
        print(f"Win - Player-{player} computer-{comp}")
        win+=1            

    elif "G" in player and "Gun" in comp:
        print(f"Draw -Player-{player} computer-{comp}")
        draw+=1
    if "G" in player and "Water" in comp:
        print(f"Lose - Player-{player} computer-{comp}")
        lose+=1
    if "G" in player and "Snake" in comp:
        print(f"Win - Player-{player} computer-{comp}") 
        win+=1

print(f"Win -{win}")
print(f"Lose -{lose}")
print(f"Draw -{draw}")
