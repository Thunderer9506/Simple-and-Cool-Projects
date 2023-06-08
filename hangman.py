import random
from urllib.request import Request, urlopen

url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()                                                    #copied from google
webpage = web_byte.decode('utf-8')
word_list = webpage.split()

word = random.choice(word_list)

length = len(word)

display = []

lives = 6

end_game = False

print("Welcome to hangman game")

stages = [''' _____________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / |
            |______________''',
            ''' _____________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      /
            |______________''',
            ''' _____________
            |/      |
            |      (_)
            |      \|/
            |       
            |      
            |______________''',
            ''' _____________
            |/      |
            |      (_)
            |      \|
            |       
            |      
            |______________''',
            ''' _____________
            |/      |
            |      (_)
            |       |
            |       
            |      
            |______________''',
            ''' _____________
            |/      |
            |      (_)
            |      
            |       
            |      
            |______________''',]

for _ in range(length):
    display += '_'

while end_game is False:
        user = input("Enter the letter: ").lower()
        for position in range(length) :
            letter = word[position]
            if letter == user:
                display[position] = letter
        print(display)

        if  user not in word:
            lives -= 1
            print(f"You have {lives} lives left,play carefully")
            print(stages[lives])
            if lives == 0:
                end_game = True
                print("You lose")
                print(f"The word was {word}")

        if '_' not in display:
            end_game = True
            print("you win")