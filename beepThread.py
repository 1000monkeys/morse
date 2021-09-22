import time
from threading import Thread
import pygame


class BeepThread(Thread):
    def __init__(self, signs, message):
        Thread.__init__(self)

        self.signs = signs
        self.message = message

        pygame.init()
        pygame.mixer.init()

        self.dot_sound = pygame.mixer.Sound('dot.wav')
        self.dash_sound = pygame.mixer.Sound('dash.wav')

        self.durationDot = int(self.dot_sound.get_length() * 1000)
        self.durationDash = int(self.dash_sound.get_length() * 1000)
        self.spaceSymbol = self.durationDot
        self.spaceLetter = self.durationDot * 3
        self.spaceWord = self.durationDot * 7

    def run(self):
        text = self.message.upper()
        letter_index = 0
        for letter in list(text):
            print(letter)
            if letter == " ":
                print("   SPACE")
                time.sleep(self.spaceWord / 1000)
            else:
                beep_index = 0
                print("LETTER: " + letter)
                for beep in self.signs[letter]:
                    if beep:
                        print("dash")
                        self.dash_sound.play()
                        pygame.time.wait(self.durationDash)
                    else:
                        print("dot")
                        self.dot_sound.play()
                        pygame.time.wait(self.durationDot)
                    if beep_index + 1 < len(self.signs[letter]):
                        print("space symbol")
                        time.sleep(self.spaceSymbol / 1000)
                    beep_index += 1
                if letter_index < len(list(text)):
                    print("space letter")
                    time.sleep(self.spaceLetter / 1000)
            letter_index += 1
