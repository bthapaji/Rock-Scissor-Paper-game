"""ROCK, SCISSOR, PAPER"""
import random
print("     WELCOME TO ROCK , SCISSOR , PAPER  GAME ")
print("     Game will  run 5 times")
print("     To win the game you have to gain highest point")
while True:
    VALUE_PLAYER = 0
    VALUE_CPU = 0
    i = 0
    while i <= 5:
        user = input("Enter your choice - ROCK,SCISSOR or PAPER -")
        action = ["scissor", "paper", "rock"]
        # generate random value for cpu
        cpu_generate = random.choice(action)
        if user == cpu_generate:
            print(f"Both players selected {cpu_generate}. It's a tie!")
        elif user == "rock":
            if cpu_generate == "scissors":
                print("Rock smashes scissors! You win!")
                VALUE_PLAYER = VALUE_PLAYER+1
            else:
                print("Paper covers rock! You lose.")
                VALUE_CPU = VALUE_CPU+1
        elif user == "paper":
            if cpu_generate == "rock":
                print("Paper covers rock! You win!")
                VALUE_PLAYER = VALUE_PLAYER + 1
            else:
                print("Scissors cuts paper! You lose.")
                VALUE_CPU = VALUE_CPU + 1
        elif user == "scissor":
            if cpu_generate == "paper":
                print("Scissors cuts paper! You win!")
                VALUE_PLAYER = VALUE_PLAYER + 1
            else:
                print("Rock smashes scissors! You lose.")
                VALUE_CPU = VALUE_CPU + 1
        i = i+1
        if i > 5:
            print("   Game Over")
            if VALUE_PLAYER > VALUE_CPU:
                print("         You Win")
                print(f"You win the game by {VALUE_PLAYER} points")
            else:
                print("         You Lose")
                print(f"CPU win the game by {VALUE_CPU} points")
    user_input = input("Do you want to play again Press(y for yes and n for no)")
    if user_input.upper() == "Y":
        print("     Welcome Again")
        continue

    print("      Thankyou for Playing  ")
    break
