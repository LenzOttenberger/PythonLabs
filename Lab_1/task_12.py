sms = int(input('Enter SMS: '))
mb = int(input('Enter MB: '))
minutes = int(input('Enter minutes: '))
summ = 24.99
if sms > 30:
    summ += (sms-30)*0.59
    print(f'SMS cost: {round((sms-30)*0.59, 2)}')
if mb > 1000:
    summ += (mb-1000)*0.79
    print(f'MB cost: {round((mb-1000)*0.79, 2)}')
if minutes > 60:
    summ += (minutes-60)*0.89
    print(f'Minutes cost: {round((minutes-60)*0.89, 2)}')
print(f'Tax: {round(summ*2/100, 2)}')
summ += summ*2/100
print(f'Final cost: {round(summ, 2)}')