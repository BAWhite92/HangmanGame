import random

class Core:
    word = ""
    progress = ""
    lives = 10
    active = True
    guessed = []

    def __init__(self):
        with open("words.txt", "r") as wordlist:
            words = wordlist.readlines()
            num = random.randint(0, len(words))
            self.word = words[num]
            for l in range(len(self.word)-1):
                self.progress += "?"
        print (f"word is {self.word}")

    def letter_guess(self):
        while self.active == True:
            if self.lives <= 0:
                print("You lose!")
                break
            letter = input("Guess a letter: ")
            if len(letter) == 1:
                if self.progress_update(letter):
                    print (self.progress)
                else:
                    self.lives -= 1
                    print (f"{letter} not in word! Lives remaining: {self.lives}")
                    guessed.append(letter)

            if "?" not in self.progress:
                print(f"You have guessed the correct word! {self.word}")
                break

    def progress_update(self, letter):
        index = 0
        present = False
        for l in self.word:
            if l == letter:
                present = True
                self.progress = (self.progress[:index] + letter +
                    self.progress[index+1:])
            index+= 1
        return present




#c = Core()
#c.letter_guess()
