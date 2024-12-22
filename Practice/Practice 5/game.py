import random
import os
from utilities import *

import random
import os
from utilities import *


class PoleChudes:
    def __init__(self, word_list, record_file):
        self.word_list = word_list
        self.record_file = record_file
        self.lives = 0
        self.initial_lives = 0
        self.current_word = ""
        self.hidden_word = ""
        self.guessed_letters = set()
        self.record = load_record(self.record_file)
        self.current_score = 0

    def choose_word(self):
        if not self.word_list:
            print("Список слов пуст. Игра завершена.")
            return False
        self.current_word = random.choice(self.word_list)
        self.word_list.remove(self.current_word)
        self.hidden_word = "■" * len(self.current_word)
        self.guessed_letters.clear()
        self.lives = self.initial_lives  # Восстановление жизней для нового слова
        return True

    def display_word(self):
        display = ''.join(
            [letter if letter in self.guessed_letters else "■" for letter in self.current_word]
        )
        return display

    def make_guess(self):
        guess = input("Введите букву или слово целиком: ").strip().lower()
        if len(guess) == 1:
            if guess in self.guessed_letters:
                print("Вы уже пробовали эту букву.")
            elif guess in self.current_word:
                print(f"Верно! Буква '{guess}' есть в слове.")
                self.guessed_letters.add(guess)
            else:
                print(f"Неверно! Буквы '{guess}' нет в слове.")
                self.lives -= 1
        elif len(guess) == len(self.current_word):
            if guess == self.current_word:
                print("Вы угадали слово целиком!")
                self.hidden_word = self.current_word
            else:
                print("Неверное слово. Игра завершена.")
                self.lives = 0
        else:
            print("Некорректный ввод. Попробуйте ещё раз.")

    def check_win(self):
        if self.hidden_word == self.current_word or set(self.current_word) <= self.guessed_letters:
            print(f"Поздравляем! Вы угадали слово: {self.current_word}")
            self.current_score += 1
            return True
        return False

    def play_round(self):
        while self.lives > 0:
            print(f"Слово: {self.display_word()} | Жизни: {self.lives}")
            self.make_guess()
            if self.check_win():
                break
        if self.lives <= 0:
            print(f"Вы проиграли. Слово было: {self.current_word}")

    def start_game(self):
        while True:
            difficulty = input("Выберите уровень сложности (легкий, средний, сложный): ").strip().lower()
            if difficulty == "легкий":
                self.lives = self.initial_lives = 7
            elif difficulty == "средний":
                self.lives = self.initial_lives = 5
            elif difficulty == "сложный":
                self.lives = self.initial_lives = 3
            else:
                print("Некорректный уровень сложности. Попробуйте ещё раз.")
                continue
            break

        while self.choose_word():
            self.play_round()
            if input("Хотите сыграть ещё раз? (да/нет): ").strip().lower() != "да":
                break

        print(f"Игра завершена. Вы угадали {self.current_score} слов.")
        if self.current_score > self.record:
            print(f"Новый рекорд: {self.current_score}")
            save_record(self.record_file, self.current_score)


if __name__ == "__main__":
    WORDS_FILE = os.path.join(os.path.dirname(__file__), "TextFiles", "words.txt")
    RECORD_FILE = os.path.join(os.path.dirname(__file__), "TextFiles", "record.txt")

    try:
        word_list = load_words(WORDS_FILE)
        game = PoleChudes(word_list, RECORD_FILE)
        game.start_game()
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")