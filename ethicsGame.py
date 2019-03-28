# Python: 3.7.3
# Author: Jamie Scott
# Purpose: Learn Python by building a simple game. 


def start(nice=0,mean=0,name=''):
    # Get the user's name
    name = describeGame(name)
    nice,mean,name = niceMean(nice,mean,name)

def getName():
    name = input('What is your name? ')
    return name

def describeGame(name):
    # Check if it's a new game or not. If it's a new user, get their info and start the game.
    # Otherwise, thank the existing user and continue with the game.

    if name != '':
        print('\nThank you for playing again, {}!'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input('\nWhat is your name? \n>>> ').capitalize()
                if name != '':
                    print('\nWelcome, {}!'.format(name))
                    print('\nIn this game, you will be greeted \nby serveral different people.')
                    print('\nYou can choose to be nice or mean, but at the end of the game, \nyour fate will be sealed by your actions.')
                    stop = False
    return name

def niceMean(nice,mean,name):
    stop = True
    while stop:
        showScore(nice,mean,name)
        pick = input('\nA stranger approaches you for a conversation. \nWill you be nice or mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print('\nThe stranger walks away smiling...')
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print('\nThe stranger glares at you menacingly and storms off...')
            mean = (mean + 1)
            stop = False
        score(nice,mean,name)

def showScore (nice,mean,name):
    print('\n{}, your current total: \n{} Nice and {} Mean'.format(name,nice,mean))

def score(nice,mean,name):
    # Score function is being passed the values stored within the 3 variables
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        niceMean(nice,mean,name)

def win(nice,mean,name):
    print('\nNice job {}, you win! \nEveryone loves you and you\'ve made lots of friends along the way!'.format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print('\nAhh too bad, game over! \n{}, you won\'t make any friends acting that way!'.format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? (Y/N) \n>>>').lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\nOh, so sad. Sorry to see you go!')
            stop = False
            quit()
        else:
            print('\nEnter (Y) for \'Yes\', or (N) for \'No\' \n>>>')

def reset(nice,mean,name): #Game starts over, reset the variables(excluding name).
    nice = 0
    mean = 0
    start(nice,mean,name)


if __name__ == '__main__':
    start()
