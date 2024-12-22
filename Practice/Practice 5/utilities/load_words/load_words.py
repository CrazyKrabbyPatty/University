import os

def load_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [line.strip().lower() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл со словами '{file_path}' не найден")
    except Exception as e:
        raise Exception(f"Ошибка при загрузке слов: {e}")