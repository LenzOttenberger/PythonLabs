nums = input("Введите список чисел через пробел: ").split()
numbers = []
for n in nums:
    if "." in n:
        numbers.append(float(n))
    else:
        numbers.append(int(n))
uniqueNumbers = []
for n in numbers:
    if numbers.count(n) == 1:
        uniqueNumbers.append(n)
duplicates = []
for n in numbers:
    if n not in uniqueNumbers and n not in duplicates:
        duplicates.append(n)
even_numbers = [x for x in numbers if isinstance(x, int) and x % 2 == 0]
odd_numbers = [x for x in numbers if isinstance(x, int) and x % 2 != 0]
negative_numbers = [x for x in numbers if x < 0]
float_numbers = [x for x in numbers if isinstance(x, float)]
sum_div5 = sum(x for x in numbers if isinstance(x, int) and x % 5 == 0)
max_num = max(numbers)
min_num = min(numbers)

print("1. Уникальные числа:", uniqueNumbers)
print("2. Повторяющиеся числа:", duplicates)
print("3. Чётные числа:", even_numbers)
print("   Нечётные числа:", odd_numbers)
print("4. Отрицательные числа:", negative_numbers)
print("5. Числа с плавающей точкой:", float_numbers)
print("6. Сумма чисел, кратных 5:", sum_div5)
print("7. Самое большое число:", max_num)
print("8. Самое маленькое число:", min_num)
