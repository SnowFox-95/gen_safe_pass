from random import *

DIGITS = '0123456789'
LOW_CHARS = 'abcdefghijklmnopqrstuvwxyz'
UP_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCT = '!#$%&*+-=?@^_.'

chars = ''


def ans_valid():
    while True:
        ans = input().lower()
        if ans == 'yes' or ans == 'да':
            return True
        elif ans == 'no' or ans == 'нет':
            return False
        else:
            print('Пожалуйста впишите Только ДА или НЕТ')
            continue


def analysis(On_digit, On_upper, On_lower, On_punct, Exclud):
    global DIGITS, LOW_CHARS, UP_CHARS, PUNCT
    str = ''
    new_str = ''
    replace_str = 'il1Lo0O'
    if On_digit == 'YES':
        str = str + DIGITS
    if On_upper == 'YES':
        str = str + UP_CHARS
    if On_lower == 'YES':
        str = str + LOW_CHARS
    if On_punct == 'YES':
        str = str + PUNCT
    if Exclud == 'YES':
        for c in range(len(str)):
            if str[c] not in replace_str:
                new_str = new_str + str[c]
    else:
        new_str = str

    return new_str


def generate_pass(l, ch):
    pas = ''
    for i in range(1, l + 1):
        c = randint(0, len(ch))
        pas = pas + ch[c]
    return pas


n = int(input('Сколько паролей необходимо?'))
len_pass = int(input('Сколько символов должен содержать пароль?'))

on_digit = 'YES'
on_upper = 'YES'
on_lower = 'YES'
on_punct = 'YES'
exclude = 'YES'

print('Включать ли цифры: 0123456789? да/нет ->')
if ans_valid():
    on_digit = 'YES'
else:
    on_digit = 'NO'
print('Включать ли заглавные символы:ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет ->')
if ans_valid():
    on_upper = 'YES'
else:
    on_upper = 'NO'
print('Включать ли заглавные символы: abcdefghijklmnopqrstuvwxyz? да/нет ->')
if ans_valid():
    on_lower = 'YES'
else:
    on_lower = 'NO'
print('Включать ли знаки пунктуации: "!#$%&*+-=?@^_." ? да/нет ->')
if ans_valid():
    on_punct = 'YES'
else:
    on_punct = 'NO'
print('Исключить ли неоднозначные символы: "il1Lo0O" ? да/нет ->')
if ans_valid():
    exclude = 'YES'
else:
    exclude = 'NO'

chars = chars + analysis(on_digit, on_upper, on_lower, on_punct, exclude)
print('Сгенерированные пароли: ')
for i in range(1, n + 1):
    print(generate_pass(len_pass, chars))
