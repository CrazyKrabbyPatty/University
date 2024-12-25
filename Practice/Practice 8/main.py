import pymorphy3
from collections import Counter
from deep_translator import GoogleTranslator
import os

file_path = os.path.join(os.path.dirname(__file__), 'source.txt')
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

morph = pymorphy3.MorphAnalyzer()
words = text.split()
normalized_words = [morph.parse(word)[0].normal_form for word in words]

word_count = Counter(normalized_words)

sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

translator = GoogleTranslator(source='ru', target='en')
translated_words = {word: translator.translate(word) for word in sorted_word_count.keys()}

with open('result.txt', 'w', encoding='utf-8') as result_file:
    result_file.write("Исходное слово | Перевод | Количество упоминаний\n")
    result_file.write("-" * 50 + "\n")
    for word, count in sorted_word_count.items():
        result_file.write(f"{word} | {translated_words[word]} | {count}\n")

print("Результаты сохранены в файле result.txt")