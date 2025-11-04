number = int(input('Enter number: '))
if number % 7 == 0:
    print('Magic number 0-0')
else:
    print(sum(map(int, str(number))))