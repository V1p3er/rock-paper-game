import random

def play():
    user = ''
    userScore = 0
    computerScore = 0
    while user != 'end':
        user = input("'r' for rock , 'p' for paper and 's' for scissors and 'end' for ending the game: ")
        randomChoice = random.choice(['r','s','p'])
        if user == randomChoice:
            print(f'Computer: {randomChoice}')
            print(f'That was tie your choice was same as computer.')
        elif user == 's' and randomChoice == 'p' or user == 'p' and randomChoice == 'r' or user == 'r' and randomChoice == 's':
            userScore +=1
            print(f'Computer: {randomChoice}')
            print(f'You won the round.')
        elif user == 's' and randomChoice == 'r' or user == 'p' and randomChoice == 's' or user == 'r' and randomChoice == 'p':
            computerScore +=1
            print(f'Computer: {randomChoice}')
            print(f'sorry you lost the round.')

    print(f'Your score: {userScore}')
    print(f'Computer score: {computerScore}')
play()
