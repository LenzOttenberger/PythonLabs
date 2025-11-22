# Создать структуру которая будет храниться следующую информация - фамилия абитуриента, балл по математике, по физике, по языку. Специальность статус поступил/непоступил. 
# Пользователь должен добавить абитру, удалить, поменять балл, статус 

users = {}
count_of_users = 0

def save(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        save_to_file()
        return None
    return wrapper

@save
def add_user(username, math, language, physics, speciality, status):
    users[username] = {'Math': math, 'Language': language, 'Physics': physics, 'Speciality': speciality, 'Status': status}
    return users[username]

def find_user(username):
    return users[username]

def edit_user_scores(username, math, language, physics):
    users[username]['Math'] = math
    users[username]['Language'] = language
    users[username]['Physics'] = physics
    
def edit_user_status(username, status):
    users[username]['Status'] = status
    
def delete_user(username):
    del users[username]
    
def save_to_file():
    with open('data.txt', '+a') as file:
        file.write('========SAVED DATA========\n')
        for k, v in users.items():
            file.write(f'==========================\n{k} statistic:\n')
            for key, value in v.items():
                file.write(f'{key}: {value}\n')
        file.close()
                
        
while True:
    print('========UNIVERSITY CAMPAING SYSTEM========')
    print('1. Add user')
    print('2. Find user')
    print("3. Edit user's scores")
    print("4. Edit user's status")
    print('5. Delete user')
    print('6. Save to file')
    print('7. Exit')
    choice = int(input('Command number: '))
    match choice:
        case 1:
            username = input('Enter username: ')
            math = int(input('Enter math score: '))
            language = int(input('Enter language score: '))
            physics = int(input('Enter physics score: '))
            speciality = input('Enter speciality: ')
            status = bool(input('Enter status (1 - passed, 0 - dont): '))
            add_user(username, math, language, physics, speciality, status)
        case 2:
            username = input('Enter username: ')
            user = find_user(username)
            print(user)
        case 3:
            username = input('Enter username: ')
            math = int(input('Enter math score: '))
            language = int(input('Enter language score: '))
            physics = int(input('Enter physics score: '))
            edit_user_scores(username, math, language, physics)
        case 4:
            username = input('Enter username: ')
            status = bool(input('Enter status (1 - passed, 0 - dont): '))
            edit_user_status(username, status)
            count_of_users -= 1
        case 5:
            username = input('Enter username: ')
            delete_user(username)
        case 6:
            save_to_file()
        case 7:
            break
