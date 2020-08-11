import re
def getIndexPositions(listElements, element) :
    index = -1
    index_list = []
    for x in listElements :
        index += 1
        if x == element:
            index_list.append(index)
    return index_list
def checkSpecial(string) :
    regex = re.compile("[@+=\-`,._!#$%^&*()?<>/\\\\|{}~:]")
    if (regex.search(string) == None) :
        return True
    else :
        return False
stickman_stages = ["""
 __________
 |     |
 |     
 |     
 |      
/ \\
"""
,
"""
 __________
 |     |
 |     O
 |     
 |     
/ \\
"""
,
"""
 __________
 |     |
 |     O
 |     |
 |     
/ \\
"""
,
"""
 __________
 |     |
 |     O
 |     |\\
 |     
/ \\
"""
,
"""
 __________
 |     |
 |     O
 |    /|\\
 |     
/ \\
"""
,
"""
 __________
 |     |
 |     O
 |    /|\\
 |      \\
/ \\
"""
,
"""
 __________
 |     |
 |     O
 |    /|\\
 |    / \\
/ \\
"""
                   ]

def main() :
    life = 6
    stick = -4
    print("Welcome to the hangman")
    while True:
        secret = input("Please enter the secret word(maximum of 10 char): ").upper()
        if secret.isalpha() and len(secret) <=10 :
            break
        else :
            print("Enter an alphabet word")
    print("secret word : ", secret)
    secretList = []
    for x in secret :
        secretList.append(x)

    print(stickman_stages[0]) #HANGMAN FIGURE
    print("Hangman Begin!")
    print("Life(s) : ", life)
    blank = ["_"] * len(secret)
    print(blank , '\n')

    while True :
        if '_' not in blank :
            print("You win! the secret word was \"",secret,"\"" )
            input("Press enter to restart\n\n")
            main()
        if life == 0:
            print("You lose. Better luck next time!")
            input("Press enter to restart\n\n")
            main()
        while True :
            guess = input("Enter a letter : ").upper()
            if any(char.isdigit() for char in guess):
                print("Enter only a single alphabet!\n")
            elif len(guess) > 1:
                print("Enter only a single alphabet!\n")
            elif guess in blank :
                print("This letter already used\n")
            else:
                break
        if guess not in secretList :
            life -= 1
            print(stickman_stages[life + stick])
            stick += 2
            if life > 0 :
                print ("Too bad, try again. ", life , " life(s) remaining\n")
        else :
            guessIndex = getIndexPositions(secretList,guess)
            for number in guessIndex :
                del blank[number]
                blank.insert(number, guess)
            print(blank , "\n")
main()
