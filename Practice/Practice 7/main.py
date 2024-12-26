import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image
import PySimpleGUI as sg


class OfficeTweaksGUI:
    def __init__(self, path):
        self.path = path

    def list_files(self, extensions=None):
        if extensions:
            return [f for f in os.listdir(self.path) if f.endswith(extensions)]
        return os.listdir(self.path)

    def pdf_to_docx(self, file):
        pdf_path = os.path.join(self.path, file)
        docx_path = pdf_path[:-4] + ".docx"
        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            sg.popup(f"Файл {file} успешно преобразован в Docx!")
        except Exception as e:
            sg.popup_error(f"Ошибка при преобразовании PDF в Docx: {str(e)}")

    def docx_to_pdf(self, file):
        docx_path = os.path.join(self.path, file)
        pdf_path = docx_path[:-5] + ".pdf"
        try:
            convert(docx_path, pdf_path)
            sg.popup(f"Файл {file} успешно преобразован в PDF!")
        except Exception as e:
            sg.popup_error(f"Ошибка при преобразовании Docx в PDF: {str(e)}")

    def compress_image(self, file, quality):
        image_path = os.path.join(self.path, file)
        try:
            image = Image.open(image_path)
            output_path = os.path.splitext(image_path)[0] + "_compressed.jpg"
            image.save(output_path, quality=quality, optimize=True)
            sg.popup(f"Файл {file} успешно сжат с качеством {quality}! Сохранён как {output_path}")
        except Exception as e:
            sg.popup_error(f"Ошибка при сжатии изображения: {str(e)}")

    def delete_file(self, file):
        try:
            os.remove(os.path.join(self.path, file))
            sg.popup(f"Файл {file} удалён!")
        except Exception as e:
            sg.popup_error(f"Ошибка при удалении файла: {str(e)}")

    def delete_files_by_criteria(self, criteria, value):
        deleted_files = []
        try:
            for file in self.list_files():
                if ((criteria == "start" and file.startswith(value)) or
                        (criteria == "end" and file.endswith(value)) or
                        (criteria == "extension" and file.endswith(value)) or
                        (criteria == "substring" and value in file)):
                    os.remove(os.path.join(self.path, file))
                    deleted_files.append(file)
            sg.popup(f"Удалены файлы: {', '.join(deleted_files)}" if deleted_files else "Нет файлов для удаления.")
        except Exception as e:
            sg.popup_error(f"Ошибка при удалении файлов: {str(e)}")

    def change_dir(self, new_path):
        if os.path.exists(new_path):
            self.path = new_path
            return True
        return False

    def run(self):
        sg.theme('DarkBlue')

        layout = [
            [sg.Text(f"Рабочий каталог: {self.path}", size=(50, 1), key='-DIR-')],
            [sg.Input(default_text=self.path, key='-DIR_INPUT-', enable_events=True, size=(40, 1)),
             sg.FolderBrowse("Browse")],
            [sg.Listbox(values=self.list_files(), enable_events=True, size=(50, 20), key='-FILE LIST-')],
            [
                sg.Button("Преобразовать PDF в Docx", size=(25, 1)),
                sg.Button("Преобразовать Docx в PDF", size=(25, 1)),
            ],
            [
                sg.Button("Сжать изображение", size=(25, 1)),
                sg.Button("Удалить файл", size=(25, 1)),
            ],
            [sg.Button("Выход", size=(10, 1))]
        ]

        window = sg.Window("Office Tweaks", layout, finalize=True)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Выход"):
                break

            if event == '-DIR_INPUT-':
                new_path = values['-DIR_INPUT-']
                if self.change_dir(new_path):
                    window['-DIR-'].update(f"Рабочий каталог: {self.path}")
                    window['-FILE LIST-'].update(self.list_files())
                else:
                    sg.popup_error("Указан неверный каталог!")

            elif event == "Преобразовать PDF в Docx":
                selected_files = values['-FILE LIST-']
                if selected_files and selected_files[0].endswith('.pdf'):
                    self.pdf_to_docx(selected_files[0])

            elif event == "Преобразовать Docx в PDF":
                selected_files = values['-FILE LIST-']
                if selected_files and selected_files[0].endswith('.docx'):
                    self.docx_to_pdf(selected_files[0])

            elif event == "Сжать изображение":
                selected_files = values['-FILE LIST-']
                if selected_files and selected_files[0].endswith(('.jpeg', '.gif', '.png', '.jpg')):
                    quality = sg.popup_get_text("Введите уровень качества (1-100):", default_text="75")
                    if quality and quality.isdigit():
                        self.compress_image(selected_files[0], int(quality))

            elif event == "Удалить файл":
                submenu_layout = [
                    [sg.Button("Удалить по начальной подстроке", size=(30, 1))],
                    [sg.Button("Удалить по конечной подстроке", size=(30, 1))],
                    [sg.Button("Удалить по расширению", size=(30, 1))],
                    [sg.Button("Удалить по подстроке", size=(30, 1))],
                ]
                submenu_window = sg.Window("Удалить файлы", submenu_layout)
                while True:
                    sub_event, sub_values = submenu_window.read()
                    if sub_event in (sg.WINDOW_CLOSED, None):
                        break
                    elif sub_event == "Удалить по начальной подстроке":
                        substring = sg.popup_get_text("Введите начальную подстроку:")
                        if substring:
                            self.delete_files_by_criteria("start", substring)
                    elif sub_event == "Удалить по конечной подстроке":
                        substring = sg.popup_get_text("Введите конечную подстроку:")
                        if substring:
                            self.delete_files_by_criteria("end", substring)
                    elif sub_event == "Удалить по расширению":
                        extension = sg.popup_get_text("Введите расширение (например, .txt):")
                        if extension:
                            self.delete_files_by_criteria("extension", extension)
                    elif sub_event == "Удалить по подстроке":
                        substring = sg.popup_get_text("Введите подстроку:")
                        if substring:
                            self.delete_files_by_criteria("substring", substring)
                submenu_window.close()

        window.close()
        exit(0)


if __name__ == "__main__":
    tweaks_gui = OfficeTweaksGUI(os.getcwd())
    tweaks_gui.run()
