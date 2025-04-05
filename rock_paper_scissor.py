import random
choices={1:"Rock",2:"Paper",3:"Scissor"}
#value from user
user_choice=int(input("enter your choice:1:rock,2:paper,3:scissor::"))
if user_choice not in choices:
    print(" you enter a invalid choice")
#values from the system
else:
    computer_choice=random.choice(list(choices.keys()))
    print(f"computer choice:{choices[computer_choice]}")
    print(f"Your choice:{choices[user_choice]}")
#logic of the game
    if(computer_choice==user_choice):
        print("it is tie!")
    elif(user_choice == 1 and computer_choice ==3) or \
        (user_choice == 2 and computer_choice ==1) or \
        (user_choice == 3 and computer_choice ==2):
        print("you will win the game:")
    else:
        print("you will loss the game")
print("thank you!!")
