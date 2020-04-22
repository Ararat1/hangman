"""
Обзор функций игры:

• getRandomWord(wordList) случайным образом выбирает одну строку из
  списка. Так выбирается слово, которое будет угадывать игрок;

• displayBoard(missedLetters, correctLetters, secretWord) отображает
  текущее состояние игры, показывает, сколько букв игрок уже предложил для определения слова, и какие из них оказались ошибочными.
  Для корректной работы этой функции необходимы три параметра.
  Строковые переменные correctLetters и missedLetter для хранения
  букв, которые были предложены игроком и тех, которых не оказалось
  в секретом слове, а также строковая переменная secretWord, содержащая секретное слово, которое пытается угадать игрок. Функция не
  возвращает каких-либо значений;

• getGuess(alreadyGuessed) проверяет, не содержится ли введенная игроком буква в строковой переменной alreadyGuessed. Функция возвращает букву, введенную игроком, если она допустима;

• playAgain() спрашивает игрока, не хочет ли он сыграть еще раз. Функция возвращает True, если игрок соглашается, или False, если отказывается

• run_game() запускает игру
"""

import random

from hangman_picks import HANGMAN_PICKS
from words import WORDS


def get_random_word(word_dict: dict) -> list:
    # Возвращает случайное слово из списка word_list

    # Во-первых, случайным образом выбираем ключ из словаря:
    word_key = random.choice(list(word_dict.keys()))

    # Во-вторых, случайным образом выбираем слово из списка ключей в словаре:
    word_index = random.randint(0, len(word_dict[word_key]) - 1)

    return [word_dict[word_key][word_index], word_key]


def display_board(missed_letters: str, correct_letters: str, secret_word: str, secret_set: str) -> None:
    print(f'Секретное слово из набора: {secret_set}')
    print(HANGMAN_PICKS[len(missed_letters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):  # заменяет пропуски отгаданными буквами
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()


def get_guess(already_guessed: str):
    """Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше."""
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()

        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in already_guessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


def play_again() -> bool:
    """Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False"""
    print('Хотите сыграть еще? (да или нет)')
    answer = input().lower().startswith('д')

    return answer


def run_game() -> None:
    print('В И С Е Л И Ц А')
    missed_letters = ''
    correct_letters = ''
    secret_word, secret_set = get_random_word(WORDS)
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word, secret_set)

        # Позволяет игроку ввести букву.
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            # Проверяет, выиграл ли игрок
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                print(f'ДА! Секретное слово - "{secret_word}"! Вы угадали!')
                game_is_done = True
                break
        else:
            missed_letters += guess

            # Проверяет, превысил ли игрок лимит попыток и проиграл.
            if len(missed_letters) == len(HANGMAN_PICKS) - 1:
                display_board(missed_letters, correct_letters, secret_word)

                message = 'Вы исчерпали все попытки!\nНе угадано букв:'
                message += f'{len(missed_letters)} и угадано букв: {len(correct_letters)}\n'
                message += f' Было загадано слово: {secret_word}.'
                print(message)

                game_is_done = True
                break

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if play_again():
        run_game()


run_game()
