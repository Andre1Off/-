import random
import sys

while True:
    print('Если хотите сыграть в "Камень, Ножницы, Бумага", напишите "играть".')
    nachalo = input()
    if nachalo == 'играть':
        letters_list: list[str] = ['Камень', 'Ножницы', 'Бумага']
        random_index = random.randint(0, len(letters_list) - 1)
        print('Напишите здесь ваш выбор.')
        tvoy_hod = input()
        print(letters_list[random_index])
        if tvoy_hod == 'Ножницы' and letters_list[random_index] == 'Ножницы':
            print('Ничья')
        elif tvoy_hod == 'Камень' and letters_list[random_index] == 'Камень':
            print('Ничья')
        elif tvoy_hod == 'Бумага' and letters_list[random_index] == 'Бумага':
            print('Ничья')
        elif tvoy_hod == 'Ножницы' and letters_list[random_index] == 'Камень':
            print('Вы проиграли')
        elif tvoy_hod == 'Ножницы' and letters_list[random_index] == 'Бумага':
            print('Вы победили!!!')
        elif tvoy_hod == 'Камень' and letters_list[random_index] == 'Ножницы':
            print('Вы победили!!!')
        elif tvoy_hod == 'Камень' and letters_list[random_index] == 'Бумага':
            print('Вы проиграли')
        elif tvoy_hod == 'Бумага' and letters_list[random_index] == 'Ножницы':
            print('Вы проиграли')
        elif tvoy_hod == 'Бумага' and letters_list[random_index] == 'Камень':
            print('Вы победили!!!')
        else:
            print('ошибка')
            sys.exit()
    else: break