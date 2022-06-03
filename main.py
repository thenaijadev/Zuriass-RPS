import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock,paper,scissors]
number = random.randint(1,3)
number-=1

computer_choice = options[number]
isValid = True

def play():
    choice = input("Rock Paper Scissors ")
    choice = choice.lower()
    if choice == "paper" and computer_choice == rock:
        choice = paper
        print(f"Computer: {computer_choice}\n You: {choice} You win.")
    elif choice == "scissors" and computer_choice == paper:
        choice = scissors
        print(f"Computer: {computer_choice}\n You: {choice} You loose.")
    elif choice == "rock" and computer_choice == paper:
        choice = rock
        print(f"Computer: {computer_choice}\n You: {choice} You loose.")
    elif choice == "rock" and computer_choice == scissors:
        choice = rock
        print(f"Computer: {computer_choice}\n You: {choice} You win.")
    elif choice == "paper" and computer_choice == scissors:
        choice = paper
        print(f"Computer: {computer_choice}\n You: {choice} You loose.")
    elif choice == "scissors" and computer_choice == rock:
        choice = scissors
        print(f"Computer: {computer_choice}\n You: {choice} You loose.")
    elif choice == "scissors" and computer_choice == scissors:
        choice = scissors
        print(f"Computer: {computer_choice}\n You: {choice} Draw.")
        play()
    elif choice == "rock" and computer_choice == rock:
        choice = rock
        print(f"Computer: {computer_choice}\n You: {choice} Draw.")
        play()
    elif choice == "paper" and computer_choice == paper:
        choice = paper
        print(f"Computer: {computer_choice}\n You: {choice} Draw.")
        play()
    else:
        print("Invalid input,Choose again.")
        play()

play()