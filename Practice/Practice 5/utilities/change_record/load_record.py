import os

def load_record(file_path):
    try:
        if not os.path.exists(file_path):
            return 0
        with open(file_path, 'r', encoding='utf-8') as file:
            return int(file.read().strip())
    except ValueError:
        return 0
    except Exception as e:
        raise Exception(f"Ошибка при загрузке рекорда: {e}")