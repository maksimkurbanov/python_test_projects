import random
import re

words = ["араб", "яблоко", "свеча", "гвоздь", "шампанское", "пузырь", "якорь", "икра", "стол", "копыто", "дуршлаг"]
bukvy = [chr(x) for x in range(ord("А"), ord("Я") + 1)]

def get_word():
    return random.choice(words).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ___$ZZZZZ$________________$$$$$$$______
            __$$$$$$$$$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            ____$$_$$_________________$$$$$$$______
            ___$$___$$________________$$$$$$$______
            ___$$___$$________________$$$$$$$______
            ___$$___$$_____________$$$$$$$$$$$$$___
            $__$$___$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
        # голова, торс, обе руки, одна нога
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ___$ZZZZZ$________________$$$$$$$______
            __$$$$$$$$$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            ____$$____________________$$$$$$$______
            ___$$_____________________$$$$$$$______
            ___$$_____________________$$$$$$$______
            ___$$__________________$$$$$$$$$$$$$___
            $__$$_______$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
        # голова, торс, обе руки
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ___$ZZZZZ$________________$$$$$$$______
            __$$$$$$$$$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __$_$$$$$_$_______________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            _______________________$$$$$$$$$$$$$___
            $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
        # голова, торс и одна рука
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ___$ZZZZZ_________________$$$$$$$______
            __$$$$$$$_________________$$$$$$$______
            __$_$$$$$_________________$$$$$$$______
            __$_$$$$$_________________$$$$$$$______
            __$_$$$$$_________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            _______________________$$$$$$$$$$$$$___
            $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
        # голова и торс
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____ZZZZZ_________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            _______________________$$$$$$$$$$$$$___
            $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
        # голова
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____$$$$$_________________$$$$$$$______
            _____$$$__________________$$$$$$$______
            ____ZZZZZ_________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            _______________________$$$$$$$$$$$$$___
            $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
        # начальное состояние
        '''
            _______________________________________
            ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
            ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            ______Z___________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            ____ZZZZZ_________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            __________________________$$$$$$$______
            _______________________$$$$$$$$$$$$$___
            $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
            _\_________/_______$$$$$$$$$$$$$$$$$$$$$
            __\_______/________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
            __________________$$$$$$$$$$$$$$$$$$$$$
        ''',
    ]
    return print(stages[tries])

def bukvy_valid(vvod):
    count = 0
    for x in vvod:
        if x in bukvy:
            count += 1
    if count == len(vvod):
        return True
    else:
        return False


def play():
    while True:
        word = get_word()
        word_completion = ['_' for _ in word]
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6

        display_hangman(tries)

        while tries > 0 and guessed == False:
            vvod = input(f'{" " * 27}{"".join(word_completion)}\n\nКакое слово загадано на табло? Назовете букву или слово целиком?'
                         f' Введите букву либо слово:\n').upper()

            while not vvod.isalpha() or bukvy_valid(vvod) == False:
                vvod = input(f"Недопустимые символы. Введите пожалуйста букву либо слово:\n").upper()

            while vvod in guessed_letters:
                vvod = input(f"Эту букву вы уже угадывали. Введите пожалуйста другую букву либо слово целиком:\n").upper()

            while vvod in guessed_words:
                vvod = input(f"Это слово вы уже угадывали. Введите пожалуйста букву либо другое слово:\n").upper()

            while len(vvod) != len(word) and len(vvod) != 1:
                vvod = input(f"Введенное слово не совпадает по длине с загаданным. Введите пожалуйста букву либо другое слово:\n").upper()

            if len(vvod) == 1:
                guessed_letters.append(vvod)
                if vvod in word:
                    print('Вы угадали! Есть такая буква в этом слове!')
                    for x in re.finditer(vvod, word):
                        word_completion[x.start()] = vvod.upper()
                        if "".join(word_completion) == word:
                            guessed = True

            else:
                guessed_words.append(vvod)
                if vvod == word:
                    word_completion = word
                    guessed = True

            if guessed == False:
                tries -= 1
                display_hangman(tries)

        if tries == 0:
            word_completion = word
            print(f'{" " * 27}{"".join(word_completion)}\n\nУвы, вам каюк! Вас повесили!')
            if input(f'\nХотите ли вы сыграть еще раз? Введите "да" чтобы продолжить играть:\n').upper() in (
                    "ДА", "Д", "L", "LF"):
                continue
            else:
                break

        if guessed == True:
            print(f'{" " * 27}{"".join(word_completion)}\n\nПоздравляю, вы угадали слово! Вы победили!')
            if input(f'\nХотите ли вы сыграть еще раз? Введите "да" чтобы продолжить играть:\n').upper() in (
                        "ДА", "Д", "L", "LF"):
                continue
            else:
                break


print(f'Добро пожаловать в капитал-шоу "Поле Чудес!"\n')

play()