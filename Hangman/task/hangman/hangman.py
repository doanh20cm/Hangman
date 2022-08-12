import random


def play(att):
    global choose, status, history, win, lost
    if att > 0:
        print("\n" + "".join(status))
        letter = input('Input a letter:')
        if len(letter) != 1:
            print('Please, input a single letter.')
            return play(att)
        if not letter.islower() or not letter.isalpha():
            print('Please, enter a lowercase letter from the English alphabet.')
            return play(att)
        if letter in history:
            print("You've already guessed this letter.")
            return play(att)
        history.append(letter)
        if letter in choose:
            for index in [index for index in range(len(choose)) if choose[index] == letter]:
                status[index] = letter
            if "".join(status) == choose:
                win += 1
                print(f'You guessed the word {choose}!\nYou survived!')
            else:
                return play(att)
        else:
            print("That letter doesn't appear in the word.")
            return play(att - 1)
    else:
        lost += 1
        print('You lost!')


def menu():
    options = ['play', 'results', 'exit']
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if choice not in options:
        return menu()
    if choice == options[0]:
        global choose, status, history
        choose = random.choice(['python', 'java', 'swift', 'javascript'])
        status = ['-'] * len(choose)
        history.clear()
        play(8)
        return menu()
    if choice == options[1]:
        print(f'You won: {win} times.\nYou lost: {lost} times.')
        return menu()


print("H A N G M A N")
choose, status, history, win, lost = '', [], [], 0, 0
menu()