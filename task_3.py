password = input('Enter password: ')
if len(password) < 16:
    print('Short password! :<')
elif password.isdigit():
    print("U'r password consist only of digits! :<")
elif password.isalpha():
    print("U'r passsword consist only of characters! :<")
else:
    print("U'r password is secure <3")
# пупупу...
