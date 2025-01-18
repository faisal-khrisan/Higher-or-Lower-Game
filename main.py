import random
from art import  logo, vs
from game_data import data
score=0
def user():
    """Function to take the user choice A or B and return user choice"""
    while True:
        try:
            choice = str(input("Who has more followers type 'A' or 'B' : "))
            if choice.lower() == 'a' or choice.lower() == 'b':
                return choice
            else:
                print("Invalid input please type 'A' or 'B' ")
        except ValueError:
            print("Invalid input please try to type 'A' or 'B' ")
def calculate_the_score(user_choice,a,b):
    """Function to calculate the score of user score gained from the correct answers and return user score"""
    global score
    if user_choice.lower() == 'a' and a > b :
         score+= 1
    elif user_choice.lower() == 'b' and  a <  b :
        score+= 1
    return score
def no_stop_game(u_choice,option1,option2):
    """Function That stop the Game if the user got a wrong answer"""
    if u_choice.lower() == 'a' and option1 > option2 :
        return  True
    elif u_choice.lower()  == 'b' and option1 < option2 :
        return True
    else:
       return False


#create random options
print(logo)
option_B = random.choice(data)
option_A = random.choice(data)
print(f"Compare A : {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
print(vs)

print(f"Compare B : {option_B['name']}, a {option_B['description']}, from {option_B['country']}")
chosen_letter = user()

stop = True
while  stop:
    print("\n" * 100)

    print(logo)


    stop = no_stop_game(chosen_letter,option_A['follower_count'], option_B['follower_count'])

    final_score = calculate_the_score(chosen_letter,option_A['follower_count'], option_B['follower_count'])

    if stop:

        option_A = option_B
        option_B = random.choice(data)
        print(f"You are right! current score : {final_score}")
        print(f"Compare A : {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
        print(vs)

        print(f"Compare B : {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

        chosen_letter = user()



    else:
        print(f"Sorry that is wrong, your final score : {final_score}")



