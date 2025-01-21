start = input("Welcome to Benedict Domination.\nTo start the game input Y to exit the game input N\nY or N: ").strip().lower()
score = 0  # Initialize score

if start == 'y':
    print("You chose to continue the adventure!")
    print("Welcome to The Office Quiz!")
    
    # Question 1
    answer = input("1. What is the name of Michael Scott's movie?\nA. Threat Level Midnight\nB. Danger Zone\nC. Goldenface\nD. Scarn's Revenge\nYour answer: ").strip().upper()
    if answer == "A":
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer is A. Threat Level Midnight.")
    
    # Question 2
    answer = input("\n2. Who does Michael hit with his car?\nA. Kevin\nB. Meredith\nC. Angela\nD. Pam\nYour answer: ").strip().upper()
    if answer == "B":
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer is B. Meredith.")
    
    # Question 3
    answer = input("\n3. What is the name of the company that buys out Dunder Mifflin?\nA. Utica Paper\nB. Sabre\nC. Prince Family Paper\nD. Vance Refrigeration\nYour answer: ").strip().upper()
    if answer == "B":
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer is B. Sabre.")
    
    print(f"\nYour final score is {score}/3.")

elif start == 'n':
    print("You chose to exit. Goodbye!")
else:
    print("Invalid input, please enter Y or N.")