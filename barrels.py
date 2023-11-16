import tkinter as tk
from tkinter import messagebox
import random
import logging

barrel_numbers = []
pulled_barrels = []
logging.basicConfig(filename='logging.log', level=logging.INFO)


def input_amount_click():
    global barrel_numbers
    # Проверка на правильность введенных данных пользователем
    try:
        # Считывание количества бочонков со строки amount
        amount_barrels = int(amount.get())
        logging.info(f"Установлено количество бочонков: {amount_barrels}")
        # Создание списка для хранения номеров бочонков в мешке
        barrel_numbers = list(range(1, amount_barrels + 1))
        # Выбор случайного номера бочонка из списка, который не будет повторятся
        random.shuffle(barrel_numbers)

        # Скрыта строка с вопросом о количестве бочонков
        # ввода количества бочонков
        # кнопка для вызова функции input_amount_click()
        label_amount.pack_forget()
        amount.pack_forget()
        input_amount.pack_forget()

        # Вызвать новую строку и кнопку "Вытащить"
        pull_label.pack(padx=10, pady=10)
        pull_button.pack(padx=10, pady=10)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите число!")
        logging.error("Ошибка при вводе количества бочонков.")


def pull_barrel():
    global barrel_numbers
    global pulled_barrels
    # Если на вход оператор получает число, то выводит строку с номером
    # бочонка и строку со всеми вытащенными бочонками
    if barrel_numbers:
        pulled_barrel = barrel_numbers.pop()
        pulled_barrels.append(pulled_barrel)
        barrel_label.config(text=f"Вы вытащили бочонок №{pulled_barrel}")
        logging.info(f"Вы вытащили бочонок №{pulled_barrel}")
        result_label.config(text=f"Были вытащены бочонки с номерами: {', '.join(map(str, pulled_barrels))}")
        logging.info(f"Были вытащены бочонки с номерами: {', '.join(map(str, pulled_barrels))}")
    # Если нет, то выводится строка, что все бочонки вытащили, кнопка становится неактивной
    else:
        barrel_label.config(text="Вы вытащили все бочонки!")
        logging.info("Все бочонки вытащены.")
        pull_button.config(state=tk.DISABLED)


# Создание окна с названием "Бочонки"
root = tk.Tk()
root.title("Бочонки")

# Вывод строки с вопросом о количестве бочонков
label_amount = tk.Label(root, text="Сколько бочонков лежит в мешке?")
label_amount.pack(padx=10, pady=10)

# Создание строки ввода количества бочонков
amount = tk.Entry(root)
amount.pack(pady=10)

# Создание кнопки для вызова функции input_amount_click()
input_amount = tk.Button(root, text="Ввод", command=input_amount_click)
input_amount.pack(pady=10)

# Строка с описанием кнопки "Вытащить"
pull_label = tk.Label(root, text="Нажмите на кнопку, чтобы вытащить бочонок")

# Кнопка "Вытащить"
pull_button = tk.Button(root, text="Вытащить", command=pull_barrel)

# Вывод строки с номером бочонка, который только что достали
barrel_label = tk.Label(root, text="")
barrel_label.pack(pady=10)

# Вывод строки со всеми бочонками, которые уже достали из мешка
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запуск окна с программой
root.mainloop()
