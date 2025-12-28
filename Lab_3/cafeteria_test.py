from cafeteria import Cafeteria

cafe = Cafeteria('meow', 4.8)
while True:
    print(f"========{cafe.name.upper()}'S CAFE========")
    print('1. Add dish to menu')
    print('2. Remove dish from menu')
    print('3. Show menu')
    print('4. Create order')
    choice = int(input('Enter your choice: '))
    match choice:
        case 1:
            print('\n')
            cafe.add_food_to_menu()
            print('\n')
        case 2:
            print('\n')
            cafe.remove_food()
            print('\n')
        case 3:
            print('\n')
            cafe.show_menu()
            print('\n')
        case 4:
            print('\n')
            cafe.create_order()
            print('\n')
        case _:
            break
