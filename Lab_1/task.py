# если длина строки больше 20 и она состоит только из цифр - найти отстаток от деления этой строки на 100, если только из букв - три последних, в противном случае высести каждый второй
string = str(input('Enter a string: '))
if len(string) > 20 and string.isdigit():
    print(f'Остаток от деления на 100: {int(string) % 100}')
elif len(string) > 20 and string.isalpha():
    print(f'Три последих символа: {string[-3::1]}')
else:
    print(f'Каждый второй символ: {' '.join(string[0::2])}')