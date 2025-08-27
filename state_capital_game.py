# Kimani Dyer, Project 2, 2.20.25
# Worked on the external documentation and logic for this project
# working on visualizing code from a writing to execute it

import random

def load_capitals(filename="capitals of states.txt"):
    # Loads the state-capital pairs from the text file into a dictionary
    capitals_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                city, state = line.rstrip().split(', ')  
                capitals_dict[state.lower()] = city
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    return capitals_dict

def get_capital(state, capitals_dict):
    # Returns the capital of the given state or an error message
    return capitals_dict.get(state.lower(), "State not found.")  

def learn_capitals(capitals_dict):
    # Interactive learning mode where users input a state and get its capital
    while True:
        state = input("Enter a state name (or type 'quiz' to start the quiz, 'exit' to quit): ").strip().lower()
        if state == 'quiz':
            return 'quiz'  
        if state == 'exit':
            return 'exit' 
        print(f"The capital of {state.title()} is {capitals_dict.get(state, 'State not found.')}.")  

def quiz_mode(capitals_dict):
    """Quiz mode: Asks users to guess the capital of randomly selected states."""
    states = random.sample(list(capitals_dict.keys()), min(5, len(capitals_dict)))  
    score = 0  
    for state in states:
        answer = input(f"What is the capital of {state.title()}? ").strip().lower()  
        if answer == capitals_dict[state].lower():  
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The capital of {state.title()} is {capitals_dict[state]}.")
    
    # Display quiz results
    print("\n----- Quiz Results -----")
    print(f"You answered {score} out of {len(states)} correctly!")

def main():
    capitals_dict = load_capitals("capitals of states.txt")  
    if not capitals_dict:
        return  
    while True:
        result = learn_capitals(capitals_dict)  
        if result == 'quiz':
            quiz_mode(capitals_dict)  
        if result == 'exit':
            print("Goodbye!")  
            break

if __name__ == "__main__":
    main()
