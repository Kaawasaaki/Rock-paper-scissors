import random

user_score = 0
computer_score = 0

options = ["rock" , "paper", "scissors"]

while True:
    
    user_input = input("Enter Rock/Paper/Scissors or q to exit: ").lower()
    
    if user_input not in options:
        continue
     
    if user_input == "q":
        break
    
    computer_pick = random.randint(0,2)
    
    computer_choice = options[computer_pick]
    
    print("Computer picks: " + computer_choice)
    
    if computer_choice == user_input:
        print("Its a draw! Continue!")
        continue
    
    if computer_choice == "rock" and user_input == "paper":
        print("User Wins!")
        user_score += 1
        
    elif computer_choice == "paper" and user_input == "scissors":
        print("User Wins!")
        user_score += 1
        
    elif computer_choice == "scissors" and user_input == "rock":
        print("User Wins!")
        user_score += 1
    
    else:
        print("Computer Wins!")
        computer_score += 1
        
    print("You have scored: " + str(user_score))
    print("Computer scored: " + str(computer_score))
    
    if user_score > computer_score:
        print("Your Winning the game!!")
    else:
        print("Your losing!!!")
  
    
    


