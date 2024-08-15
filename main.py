import os
import random
import shutil
import sys
import time


class format:
   END = '\033[0m'
   BOLD = '\033[1m'
   FADE = '\033[2m'
   ITALIC = '\033[3m'
   UNDERLINE = '\033[4m'
   SWAP = '\033[7m'

class functions:
   def scrolltext(self,text):
      for character in text:
         sys.stdout.write(character)
         sys.stdout.flush()
         time.sleep(0.03)

   def getConsoleWidth(self):
      return shutil.get_terminal_size((80, 24)).columns

   def printTitle(self):
      title = f"{format.UNDERLINE}{format.BOLD}Hangman Game{format.END}"
      print(title.center(self.getConsoleWidth() + 13))
      print("\n")

class game:
   def __init__(self): #randomwordgenerator.com
      self.random_words = ["theme","frequency","offender","overcharge","technology",
                      "prestige","delete","emergency","superintendent","inflation",
                      "anxiety","morsel","pitch","beautiful","sacrifice",
                      "worth","statement","vertical","sequence","tension",
                      "bottle","intervention","correspond","constant","request",
                      "technique","civilization","falsify","bloodshed","voucher",
                      "tribute","exercise","include","cabin","return",
                      "overeat","discreet","timber","dignity","syndrome",
                      "sphere","sausage","subway","solution","explain",
                      "belief","characteristic","background","problem","hardship",
                      "photography","project","referee","singer","invasion",
                      "island","housewife","occupy","improve","biography",
                      "presidency","loyalty","correspondence","public","pastel",
                      "parameter","transport","paralyzed","stream","imperial",
                      "mother","opponent","progress","polish","retreat",
                      "available","discount","treatment","freighter","injection",
                      "scratch","physical","maximum","pigeon","literature",
                      "doctor","cassette","rehabilitation","identification","negotiation",
                      "intermediate","responsibility","operational","organisation",
                      "constituency","communication","revolutionary","homosexual",
                      "characteristic","recommendation","sensitivity","examination",
                      "association","credibility","civilization","earthwax",
                      "cooperative","vegetarian","supplementary","diminishing",
                      "refrigerator","ambiguity","orientation","cooperation",
                      "ideology","discrimination","continuation","qualification",
                      "disability","administration","possibility","environmental",
                      "hospitality","nationalism","deteriorate","archaeological",
                      "liability","investigation","beneficiary","constitutional",
                      "personality","extraterrestrial","enthusiasm","multimedia",
                      "anticipation","enfix","contemporary","restaurant",
                      "overweight","untrustworthy","randomisation","installations",
                      "constellation","entertainment","reproduction","memorandum",
                      "economics","repetition","imperial","consultation",
                      "epicalyx","affinity","concentration","revolution",
                      "exhibition","introduction","particular","integrated",
                      "humanity","refrigeration","motivation","cooperate",
                      "resolution","notorious","relaxation","constitution",
                      "exaggerate","eliminate","isolation","generation",
                      "conservation","relationship","representative","interactive",
                      "apology","articulate","hypothesis","spontaneous",
                      "legislature","dictionary","mechanism","photography",
                      "temporary","competition","charismatic","respectable",
                      "harmful","neighborhood","hypnothize","regulation",
                      "audience","default","ecstasy","modernize","excavate",
                      "selection","perception","digress","shallow","mislead",
                      "platform","proportion","earthquake","cigarette",
                      "custody","reasonable","projection","conspiracy","passive",
                      "curriculum","outline","premature","cruelty","forestry",
                      "meeting","articulation","monster","imposter","addicted",
                      "dependence","landlord","creation","presidential",
                      "convulsion","intention","wedding","pioneer","emphasis",
                      "scratch","deposit","squeeze","trustee","undertake",
                      "information","situation","ministry","original","minimum",
                      "desire","obligation","umbrella","overview","operations",
                      "fatality","architecture","spontaneity","marathon",
                      "intervening","secretive","disciplinary"]
      random_select = random.randint(1, len(self.random_words))
      
      self.random_word = self.random_words[random_select]
      self.guessed_letters = []
      self.display_word = ""
      self.end = False
      self.running = True
      self.wrong_guesses = 0
   
   def getInput(self):
      while True:
         message = ""
         try:
            guessed_letter = input("Enter your guess: ")
            if not guessed_letter.isalpha() or len(guessed_letter) != 1:
               message = "Please enter a singular letter as your guess."
               raise ValueError
            elif guessed_letter.upper() in self.guessed_letters:
               message = "Please do not repeat guesses."
               raise ValueError
            break
         except ValueError:
            os.system('clear')
            self.display()
            print(format.ITALIC + message + format.END)
      if guessed_letter not in self.random_word:
         self.wrong_guesses += 1
      self.guessed_letters.append(guessed_letter.upper())

   def display(self):
      instance = functions()
      os.system('clear')
      instance.printTitle()
      display_identifier = f"stage{self.wrong_guesses}"
      art_stage = getattr(hangman_stages, display_identifier)
      print(art_stage)
      time.sleep(0.5)
      print("\n")
      if len(self.guessed_letters) == 0:
         functions().scrolltext("_" * len(self.random_word))
      instance.scrolltext(self.display_word)
      time.sleep(0.7)
      print()
      print(f"{format.BOLD}\nLength of word: {len(self.random_word)}")
      if len(self.guessed_letters) > 0:
         print(f"Guessed letters: {', '.join(self.guessed_letters)}")
      else:
         print("Guessed letters: N/A")
      print(f"Wrong guesses left: {6 - self.wrong_guesses}{format.END}")
      print()

   def checkLose(self):
      if self.wrong_guesses == 6:
         self.display()
         functions().scrolltext(f"The word was: {self.random_word.title()}")
         self.running = False

   def checkWin(self):
      if self.display_word == self.random_word.upper():
         self.display()
         functions().scrolltext("Well done. You won!")
         self.running = False

   def main(self):
         while self.running:
            self.display()
            self.getInput()
            self.display_word = ""
            for character in self.random_word:
               if character.upper() in self.guessed_letters:
                  self.display_word += character.upper()
               else:
                  self.display_word += "_"
            self.checkWin()
            self.checkLose()

class hangman_stages:
   stage0 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''
   stage1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
   stage2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
   stage3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
   stage4 = '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========='''
   stage5 = '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========='''
   stage6 = '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''

if __name__ == "__main__":
   game().main()
