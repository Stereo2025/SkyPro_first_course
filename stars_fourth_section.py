# 1 -Точное время 2

# s = input(': ')
# if s.count('.') == 1:
#     print(f"{s.count('*')}:15")
# elif s.count('.') == 2:
#     print(f"{s.count('*')}:30")
# elif s.count('.') == 3:
#     print(f"{s.count('*')}:45")
# else:
#     print(f"{s.count('*')}:0")

# 2. Надежный пароль

# import re
#
# login = input(': ')
# lst = []
# if len(login) < 3:
#     print('Логин должен содержать больше 3 символов.')
#     quit()
# passwrd = input(': ')
# if len(passwrd) < 8:
#     print('Пароль должен содержать больше 8 символов.')
# x = re.findall('[0-9]', passwrd)
# if len(x) < 0:
#     print('Пароль должен содержать хотя бы одну цифру')
# elif len(x) > 0 and len(passwrd) > 8:
#     print('Это хорошие логин и пароль!')


# 3 - Шифр номер четыре
# print("Рооз наа фмдиц а ывч ыва оо ивкр ьке пвшпрце уенпвта"[3::4])


# 4 - Скрытое сообщение

# message = 'Мн3 4у9ится, 4т0 кт0-т0 4итает с006щения!!! ' \
#           'М0ж3т я 8се при9умала, н0 6у9ь на43ку, 0к?'
# s = message.replace('3', 'е').replace('4', 'ч').replace('6', 'б')\
#     .replace('8', 'в').replace('9', 'д').replace('0', 'о')
# print(s)


# 5 - Почта на корпоративном домене

# mail = input(': ')
# if mail.endswith('.ru'):
#     print('Это почта, она на бесплатном домене')
# elif mail.endswith('.com'):
#     print('Это почта, она на корпоративном домене')
# else:
#     print('Это вообще не почта')

# 6 - Игра в города


# 7 Азбука морзе Щелк - щелк
# morza = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
#          '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#          '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', ' ': ' '}
#
# for i in input(': ').split():
#     print(' '.join(morza[c] for c in i.upper()))
#
# result = dict([val, key] for key, val in morza.items())
# print(''.join([result[i] for i in input('>: ').split()]))


# 8 - Кто чем занимается?

# user = input(': ')
# d = {
#     'Мария А': 'Фронтендер',
#     'Алексей А': 'Фронтендер',
#     'Иван Б': 'Бэкендер',
#     'Тоня И': 'Бэкендер',
#     'Дарья У': 'Тестировщик',
#     'Валерия К': 'Бэкендер'}
# for k, v in d.items():
#     if user == v:
#         print(k)


# 9 - Замечательные соседи

# my_dict = {
#     1: 'гелий',
#     2: 'магний',
#     3: 'цинк',
#     4: 'никель',
#     5: 'медь',
#     6: 'водоворот'}
# user = int(input(': '))
#
# left = my_dict[user - 1]
# right = my_dict[user + 1]
#
# print(f'{user} это {my_dict[user]}\n'
#       f'Соседи: \n{user - 1} это {left}\n'
#       f'{user + 1} это {right}')


# 10 - Радиоротация

# lst = ['Galibri & Mavik - Federiko Felini', 'DaBro - На Часах Ноль-Ноль',
#        'Dead Blonde - Мальчик На Девятке', 'Султан Лагучев - Горький Вкус',
#        'Galibri & Mavik - Federiko Felini']
# print({i: lst.count(i) for i in lst})


# 11 - Слово на букву

# lst = []
# for i in range(10):
#     lst.append(input(': ').upper()[0])
# result = {i: lst.count(i) for i in lst}
# for k, v in result.items():
#     print(f'{k} - {v} слов' for k, v in result.items())


# 12 - Частотный список

# user = 'Если «если» перед «после», значит «после» после «если». ' \
#        'Если «если» после «после», значит «после» перед «если».'.lower()
# new = user.replace('!', '').replace('?', '').replace(',', '')\
#     .replace('.', '').replace('«', '').replace('»', '').replace('-', '').split()
# res = {i: new.count(i) for i in new}
# print(f'Всего слов: {len(new)}')
#
# for k, v in res.items():
#     print(f'{k} - {v}')


# 13. Список поступивших
# std = {
#     'Мария А.': 55,
#     'Алексей А.': 78,
#     'Иван Б.': 82,
#     'Тоня И.': 79,
#     'Дарья У.': 62,
#     'Валерия К.': 69,
#
# }
# user = int(input(': '))
# yes, no = [], []
#
# for k, v in std.items():
#
#     if user <= v:
#         yes.append(k)
#
#     elif user >= v:
#         no.append(k)
#
# print("Поступили:")
# print('\n'.join(yes))
# print()
# print('Не поступили:')
# print('\n'.join(no))

