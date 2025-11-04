summ = int(input('Enter summ: '))
ruble100 = summ // 100
summ -= ruble100 * 100
ruble50 = summ // 50
summ -= ruble50 * 50
ruble10 = summ // 10
summ -= ruble10 * 10
ruble5 = summ // 5
summ -= ruble5 * 5
ruble2 = summ // 2
summ -= ruble2 * 2
ruble1 = summ // 1
summ -= ruble1 * 1
print(f'100rub: {ruble100}, 50rub: {ruble50}, 10rub: {ruble10}, 5rub: {ruble5}, 2rub: {ruble2}, 1rub: {ruble1}')
