import  numpy as np

months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

expenses = np.array([1, 3, 2, 7, 6, 1, 1, 4, 7, 8, 9, 2])

winter_expenses = np.sum(expenses[[0, 1, 11]])
summer_expenses = np.sum(expenses[5:8])

if summer_expenses < winter_expenses:
    print('Expenses are highest in winter period.')
elif summer_expenses == winter_expenses:
    print('Expenses are equal for both of periods.')
else:
    print('Expenses are highest in summer period.')

indexes_of_three_highest_expenses_months = np.argsort(expenses)[-3:]
print('Three the most expensive months are:')
for index in indexes_of_three_highest_expenses_months:
    print(f'{months[index]}: {expenses[index]}')