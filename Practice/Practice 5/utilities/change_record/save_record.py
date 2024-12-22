def save_record(file_path, score):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(score))
    except Exception as e:
        raise Exception(f"Ошибка при сохранении рекорда: {e}")
