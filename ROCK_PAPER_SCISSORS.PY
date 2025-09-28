import random

# ASCII art for moves
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

images = [Rock, Paper, Scissors]

# User input
user_choice = int(input("Choose your move! Enter 0 for Rock 🪨, 1 for Paper 📄, or 2 for Scissors ✂️:\n"))

# Check valid input
if user_choice < 0 or user_choice > 2:
    print("❌ Invalid choice. Please pick 0, 1, or 2 next time!")
else:
    print(f"\nYou chose:\n{images[user_choice]}")

    # Computer choice
    computer_choice = random.randint(0, 2)
    print(f"\nComputer chose:\n{images[computer_choice]}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a Draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("🎉 You win! Rock crushes Scissors.")
    elif user_choice == 2 and computer_choice == 1:
        print("🎉 You win! Scissors cut Paper.")
    elif user_choice == 1 and computer_choice == 0:
        print("🎉 You win! Paper covers Rock.")
    else:
        print("💀 You lose!")
