# класс буфет с методами добавить блюдо, удалить блюдо, блюдо с ценной, составить заказ, напечатать чек

class Cafeteria:
    def __init__(self, name='', rating=0.0, snack_menu=[], dish_menu=[], drink_menu=[]):
        self._name = name
        self._rating = rating
        self._snack_menu = snack_menu
        self._dish_menu = dish_menu
        self._drink_menu = drink_menu
        
    @property
    def name(self):
        return self._name
    
    @property
    def rating(self):
        return self._rating
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(f'Value {value} not a string!')
        self._name = value
        
    @rating.setter
    def rating(self, value):
        if not isinstance(value, float):
            raise TypeError(f'Value {value} is not a string!')
        self._rating = value
        
    def add_food_to_menu(self):
        food = Food()
        print('=====FOOD CREATION=====')
        while True:
            try:
                food_name = input("Enter food's name: ")
                food.name = food_name
                break
            except TypeError:
                print('Ha-ha-ha, u have type error T-T')
            except ValueError:
                print(f"Value is empty!")
        while True:
            try:
                food_type = input("Enter food's type (snack, dish, drink): ")
                food.type = food_type
                break
            except TypeError:
                print('Ha-ha-ha, u have type error T-T')
            except ValueError:
                print('Oh no, bro, u have value error T-T')
        while True:
            try:
                food_cost = float(input("Enter food's cost (like 0.8 or 45): "))
                food.cost = food_cost
                break
            except TypeError:
                print('Ha-ha-ha, u have type error T-T')
            except ValueError:
                print('Oh no, bro, u have value error T-T')
        match food._type:
            case 'snack':
                self._snack_menu.append(food)
            case 'dish':
                self._dish_menu.append(food)
            case 'drink':
                self._drink_menu.append(food)
        print("Dish successfuly added to menu!")
        
    def remove_food(self):
        print('=====REMOVE FOOD=====')
        while True:
            food_name = input("Enter food's name: ")
            if food_name in self.snack_menu:
                self._snack_menu.remove(food_name)
                break
            elif food_name in self.dish_menu:
                self._dish_menu.remove(food_name)
                break
            elif food_name in self.drink_menu:
                self._drink_menu.remove(food_name)
                break
            print(f"Food named {food_name} doesn't exist! Try again!")
        
    def show_menu(self):
        print(f"====={self._name.upper()}'S MENU=====")
        print("SNACKS ->\n")
        for i in self._snack_menu:
            print(f'{i.name} {i.cost}')
        print("\nDIDSHES ->\n")
        for i in self._dish_menu:
            print(f'{i.name} {i.cost}')
        print("\nDRINKS ->\n")
        for i in self._drink_menu:
            print(f'{i.name} {i.cost}')
            
    def find_food_cost(self, value):
        for i in self._snack_menu:
            if value == i.name:
                return i.cost
        for i in self._dish_menu:
            if value == i.name:
                return i.cost
        for i in self._drink_menu:
            if value == i.name:
                return i.cost
        return 0
            
    def create_order(self):
        print('=====CREATE ORDER=====')
        order = Order()
        bill = 0.0
        self.show_menu()
        while True:
            print("\nCURRENT ORDER ->")
            for k, v in order.dishes.items():
                print(f"{k}, count {v}")
            print('1. Add dish')
            print('2. Remove dish')
            print(f'3. Pay {bill}')
            choice = input('Enter number of command: ')
            food_name = ''
            count = 0
            match choice:
                case '1':
                    while True:
                        try:
                            food_name = input("Enter food's name: ")
                            food_price = self.find_food_cost(food_name)
                            if food_price != 0:
                                count = int(input("Enter count: "))
                                bill += food_price * count
                                order.dishes[food_name] = count
                                break
                        except ValueError:
                            print("Value error. Try again.")
                case '2':
                    while True:
                        food_name = input("Enter food's name: ")
                        if food_name in order.dishes:
                            bill -= self.find_food_cost(food_name) * order.dishes[food_name]
                            del order.dishes[food_name]
                            break
                        print('Invalid Key!')
                case '3':
                    with open('bill.txt', 'w+') as file:
                        file.write(f"====={self.name}'S BILL=====\n")
                        for k, v in order.dishes.items():
                            file.write(f"{k}, count {v}\n")
                        file.write(f"Total cost: {bill}")
                        file.close()
                    break
                        
        
class Food:
    def __init__(self, name='', type='', cost=0.0):
        self._name = name
        self._type = type
        self._cost = cost
        
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type
    
    @property
    def cost(self):
        return self._cost
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(f"Value {value} is empty!")
        if not isinstance(value, str):
            raise TypeError(f'Value {value} is not a string!')
        self._name = value
        
    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Value {value} is not a string!')
        elif value not in ['snack', 'dish', 'drink']:
            raise ValueError(f'Value {value} is not a type!')
        self._type = value.lower()
        
    @cost.setter
    def cost(self, value):
        if not isinstance(value, float):
            raise TypeError(f'Value {value} is not a string!')
        if value < 0.01 or value > 100:
            raise ValueError(f'Value {value} is unreal cost, man!')
        self._cost = value
        
        
class Order:
    def __init__(self, number=0):
        self._number = number
        self._dishes = {}
        
    @property
    def number(self):
        return self._number
    
    @property
    def dishes(self):
        return self._dishes
    
    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Value {value} is not int!')
        self._number = value