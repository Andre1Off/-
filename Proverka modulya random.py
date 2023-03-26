import random

print('А теперь тебе предстоит сразится с самим Лордом Волдемортом!')
print('Используй защитное заклинание "Протего" и атакующие заклинания "Экспеллиармус" или "Авада кедавра"')
print('...')
print('...')
print('...')
print('...')
print('...')
print('Авада кедавра!')
waiting = input()
zaclenanie = input()
if waiting == 'Протего' and zaclenanie == 'Экспеллиармус' or zaclenanie == 'Авада кедавра':
    letters_list: list[str] = ['Увы, Воллдеморт смог защититься от вашего заклинания и убить вас', 'Поздравляю вас! Вы победили самого Лорда Волдеморта! Теперь вы стали самым величайшим волшебником в мире!']
    random_index = random.randint(0, len(letters_list) - 1)
    print(letters_list[random_index])
else:
    print('Увы, вы мертвы')