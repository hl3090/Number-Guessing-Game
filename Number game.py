import random

title ="""
                 Welcome to the Guess a Number Game
"""
print(title)

level = 1

while True:
    if level == 1:
        start = 1
        end = 100
    elif level == 2:
        start = 1
        end = 200
    elif level == 3:
        start = 1
        end = 300        
    else:
        break
    
    computer = random.randint(start,end)
    
    for i in range(1,6):
        user = int(input("Guess a number between {} to {}: ".format(start,end)))
        
        if computer > user:
            print("Guess a higher number")
        elif computer < user:
            print("Guess a lower number")    
        else:
            print(f"You Won level {level}".format(level))
            level += 1
            print()
            print(f"Level {level} begins: ")
            break
        
    else:
        print("You have lost!!....Correct Number is: ",computer) 
        user_choice = input("Do you want to play again!......if yes press y if no press n: ")
        if user_choice == 'y':
            print()
            level = 1
        else:
            print()
            print("Hope You Enjoyed this game!!\U0001F917")
            print("THANK YOU\U0001F607")
            break
        
    if level > 3:
        print("Congratulations!! You have cleared all the levels") 
        break            
                
