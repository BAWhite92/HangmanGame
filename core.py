import random

class Core:
    word = ""
    progress = ""

    def __init__(self):
        with open("words.txt", "r") as wordlist:
            words = wordlist.readlines()
            num = random.randint(0, len(words))
            self.word = words[num]
            for l in range(len(self.word)-1):
                self.progress += "?"
        print (f"word is {self.word}")
        print(f"guess is {self.progress}")

    def letter_guess(self):
        active = True
        while active == True:
            letter = input("Guess a letter: ")
            if len(letter) == 1:
                index = 0
                for l in self.word:
                    if l == letter:
                        self.progress = (self.progress[:index] + letter +
                            self.progress[index+1:])
                    index+= 1
                print (self.progress)
            if "?" not in self.progress:
                print(f"You have guessed the correct word! {self.word}")
                active = False





c = Core()
c.letter_guess()
