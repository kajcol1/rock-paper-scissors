import random

print("\n...ROCK....... \n...PAPER...... \n...SCISSORS...")
print("\n::: PROVIDE 'q' TO EXIT ::: \n")

game = ("rock", "paper", "scissors")
player1 = " "

def rps(player1):
    if player1 == "rock" and player2 == "paper":
        return "You win!"
    elif player2 == "rock" and player1 == "paper":
        return "You lost!"
    elif player1 == "rock" and player2 == "scissors":
        return "You win!"
    elif player2 == "rock" and player1 == "scissors":
        return "You lost!"
    elif player2 == "paper" and player1 == "scissors":
        return "You win!"
    elif player1 == "paper" and player2 == "scissors":
        return "You lost!"
    else:
        return "DEAD HEAT"    

while player1 != "q":
    player1 = input("rock, paper, scissors?: ")
    player2 = random.choice(game)

    if player1 in game or player1 == "q":
        print(rps(player1))
        print(f"Player1: {player1} and Player2: {player2}")
        
    else: 
        print("!!! ERROR, provide rock, paper, scissors or 'q' to exit !!!")
