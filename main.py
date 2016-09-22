#!/usr/bin/python3
from random import randint
from enum import Enum
import os
import re


class Forca(object):
    def __init__(self):
        self.sortedWord = ''
        self.sortedType = ''
        self.lettersCount = 0
        self.lstWordLetters = []
        self.lstAttemptedLetters = []
        self.tryesLeft = 6

    def sortWord(self):
        try:
            with open('words.txt') as f:
                self.tryesLeft = 6
                content = f.read()
                words = len(content.splitlines())
                word = int(randint(0, words))
                contentWords = content.splitlines()

                self.sortedWord = contentWords[word-1].split('-')[0].strip()
                self.sortedType = contentWords[word-1].split('-')[1].strip()
                self.lettersCount = len(self.sortedWord)
                self.lstWordLetters = ['_' for x in range(self.lettersCount)]


            return True
        except IOError:
            print('Lista de palavras nao encontradas')
            return False

    def tryLetter(self, letter):
        if (letter in self.lstAttemptedLetters):
            print('Letra já tentada')
            return True
        self.lstAttemptedLetters.append(letter)
        letters = list(self.sortedWord.strip())

        found = False
        i = 0
        for r in letters:
            if r == letter:
                found = True
                self.lstWordLetters[i] = r
            i = i + 1
        return found

    def tryWord(self, word):
        if (word in self.lstAttemptedLetters):
            print('Letra já tentada')
            return True
        self.lstAttemptedLetters.append(word)
        if word == self.sortedWord:
            letters = list(self.sortedWord.strip())
            i = 0
            for r in letters:
                self.lstWordLetters[i] = r
                i = i + 1
        return word == self.sortedWord

    def foundWord(self):
        return ''.join(self.lstWordLetters) == self.sortedWord


    def decrementTryes(self):
        self.tryesLeft = self.tryesLeft - 1


    def chancesOver(self):
        return self.tryesLeft <= 0


    def printForca(self):
        print('\n')
        print('-' * 7)
        print('|     |')
        print(str.format('|     {0}', ' ' if self.tryesLeft == 6 else '0'))
        print(str.format('|    {1}{0}{2}', '|' if self.tryesLeft < 5 else ' ',\
                         '/' if self.tryesLeft < 4 else ' ', \
                         '\\' if self.tryesLeft < 3 else ' '
                         ))
        print(str.format('|    {0} {1}', \
                        '/' if self.tryesLeft < 2 else ' ', \
                        '\\' if self.tryesLeft < 1 else ' '
                         ))
        print('|')


class INPUT_TYPE(Enum):
    NUMBER = 1
    STRING = 2
    WORD = 3

    def __str__(self):
        return self.name

def getInput(inputType):
    input_str = ''
    if inputType == INPUT_TYPE.NUMBER:
        while not re.match("^[0-9]{1}$", input_str):
            input_str = input(">> ")
    elif inputType == INPUT_TYPE.STRING:
        while not re.match("^[a-z]{1}$", input_str):
            input_str = input(">> ")
    elif inputType == INPUT_TYPE.WORD:
        while not re.match("^[a-z]+$", input_str):
            input_str = input(">> ")
    return input_str


def main():
    while True:
        word = Forca()
        if word.sortWord():
            while True:
                print(str.format('Dica da palavra é {0} com {1} letras', word.sortedType.strip(), word.lettersCount))
                if len(word.lstAttemptedLetters) > 0:
                    print('Letras já sorteadas')
                    print(' '.join(word.lstAttemptedLetters))

                word.printForca()

                print(' '.join(word.lstWordLetters))

                print('\n')
                print('Digite 1 para chutar letra ')
                print('Digite 2 para chutar a palavra ')
                print('Digite 3 para revelar a palavra ')
                print('Digite 4 para desistir ')

                opt = getInput(INPUT_TYPE.NUMBER)

                found = False

                print('\n')
                if int(opt) == 1:
                    print('Letra ')
                    letter = getInput(INPUT_TYPE.STRING)
                    found = word.tryLetter(letter)
                elif int(opt) == 2:
                    print('Palavra ')
                    wrd = getInput(INPUT_TYPE.WORD)
                    found = word.tryWord(wrd)
                elif int(opt) == 3:
                    print(str.format('A palavra é: {0}', word.sortedWord))
                    break
                elif int(opt) == 4:
                    break

                if not found:
                    word.decrementTryes()

                if word.chancesOver():
                    print('\n')
                    print('Suas chances acabaram')
                    print(str.format('A palavra é: {0}', word.sortedWord))
                    break
                elif word.foundWord():
                    print('Encontrou a palavra :)')
                    print('\n')
                    print(str.format('Palavra: {0}', word.sortedWord))
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')

        print('\n')
        print('Digite 1 para sair')
        print('Digite 2 para sortear uma palavra')
        exit = getInput(INPUT_TYPE.NUMBER)

        if int(exit) == 1:
            print('Tchau')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
