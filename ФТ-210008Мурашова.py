import logging
import random
import sys

logging.basicConfig(level=logging.INFO, filename="log_file.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")

# Ввод числа пользователем.
def input_num(text, min_num = 1):
    while True:
        try:
            logging.info(text)
            num = int(input(text))
            logging.info(f'Пользователь ввел: {num}')
        except:
            print('Неверно введенно число. Попробуйте ещё раз!')
            logging.error('Введенное значение пользователем было неверным', exc_info=True)
            continue

        if num < min_num:
            print(f'Число должно быть больше {min_num-1}. Попробуйте ещё раз!')
            logging.error('Введенное число было меньше 1')
            continue

        logging.info(f'Верно введенное число пользователем: {num}')
        return num

# Ввод максимального числа для загадывания и количество попыток.
max_num = input_num('Введите максимальное число для загадывания: ', 2)
amount = input_num('Введите количество попыток: ')
# Загадывание числа.
num = random.randint(1, max_num)
logging.info(f'Загаданное число {num}')

# Попытки отгадать число.
for i in range(amount):
    current_num = input_num('Введите число для отгадывания: ')

    if current_num < num:
        print('Число меньше загаданного!')
        logging.info(f'Введенное число меньше загаданного')
    elif current_num > num:
        print('Число больше заданного!')
        logging.info(f'Введенное число больше загаданного')
    else:
        print('Вы отгадали число!')
        logging.info(f'Число было отгадано')
        sys.exit()

# Попытки отгадать число закончились.
print(f'Попытки закончились! Загаданное число: {num}')
logging.info(f'У пользователя закончились попытки')