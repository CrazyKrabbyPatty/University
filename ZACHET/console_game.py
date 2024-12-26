from random import *
from datetime import *

class RockPaperScissors:

    def RandomObject(self, file):
        Objects = ['камень', 'ножницы', 'бумага']
        ObjChoice = choice(Objects)
        file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Компьютер выбрал {ObjChoice} \n")
        return ObjChoice

    def GetPlayerChoice(self, file):
        info = [
            "\n"
            "Сделайте выбор: \n"
            "1 - камень \n"
            "2 - ножницы \n"
            "3 - бумага \n"
        ]
        print(*info)
        obj = {1:"камень", 2:"ножницы", 3:"бумага"}
        while True:
            playerChoice = int(input())
            if playerChoice in obj:
                print(f"Ваш выбор - {obj[playerChoice]}")
                file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Игрок выбрал {obj[playerChoice]} \n")
                return obj[playerChoice]
            else:
                print("Неверный ввод")

    def CheckWin(self, obj, ply):
        if obj == ply:
            return "draft"
        if obj == "камень":
            if ply == "ножницы":
                return "Player_Lose"
            else:
                return "Player_Win"
        if obj == "ножницы":
            if ply == "камень":
                return "Player_Lose"
            else:
                return "Player_Win"
        if obj == "бумага":
            if ply == "камень":
                return "Player_Lose"
            else:
                return "Player_Win"

    def RunGame(self):
        file = open("logs.txt", "a", encoding="utf-8")
        file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Начало игры \n")
        menu = [
            "\n"
            "Действия \n"
            "0 - Выход из игры \n"
            "1 - Играть \n"
        ]
        wins_in_a_row = 0
        while True:
            print(*menu)
            player_input = int(input("Выберите действие: "))

            if player_input == 0:
                print("Выход из игры")
                print(f"Всего побед подряд: {wins_in_a_row}")
                file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Конец игры \n")
                file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Рекордная серия {wins_in_a_row} \n")
                file.close()
                break

            elif player_input == 1:
                obj = self.RandomObject(file)
                ply = self.GetPlayerChoice(file)
                result =self.CheckWin(obj, ply)
                if result == "Player_Lose":
                    print("Игрок проиграл!")
                    file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Игрок проиграл! \n")
                    wins_in_a_row = 0

                elif result == "Player_Win":
                    file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Игрок выиграл! \n")
                    wins_in_a_row += 1
                    print("Игрок победил!")
                else:
                    file.write(f"[{datetime.now().strftime("%H:%M:%S")}] Ничья! \n")
                    print("Ничья!")
            else:
                print("Введите корректное действие")

if __name__ == "__main__":
    RockPaperScissors().RunGame()