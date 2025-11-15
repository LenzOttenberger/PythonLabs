import uuid

EXCHANGE_RATES = {
    "USD": {"USD": 1.0, "EUR": 0.94, "BYN": 3.25, "RUB": 96.0, "CNY": 7.3, "GBP": 0.82},
    "EUR": {"USD": 1.06, "EUR": 1.0, "BYN": 3.45, "RUB": 102.0, "CNY": 7.75, "GBP": 0.87},
    "BYN": {"USD": 0.31, "EUR": 0.29, "BYN": 1.0, "RUB": 29.5, "CNY": 2.25, "GBP": 0.25},
    "RUB": {"USD": 0.010, "EUR": 0.0098, "BYN": 0.034, "RUB": 1.0, "CNY": 0.076, "GBP": 0.0085},
    "CNY": {"USD": 0.137, "EUR": 0.129, "BYN": 0.44, "RUB": 13.1, "CNY": 1.0, "GBP": 0.11},
    "GBP": {"USD": 1.22, "EUR": 1.15, "BYN": 4.0, "RUB": 117.5, "CNY": 9.1, "GBP": 1.0},
}


class Bank:
    def __init__(self, name):
        self.__name = name
        self.__clients = {}

    def create_client(self, first_name, second_name):
        new_client = Client(first_name, second_name)
        self.__clients[new_client.get_client_id()] = new_client
        return new_client

    def get_clients(self):
        return dict(self.__clients)

    def get_name(self):
        return self.__name


class Client:
    def __init__(self, first_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__client_id = uuid.uuid4()
        self.__accounts = {}

    def open_account(self, currency):
        if currency not in self.__accounts:
            new_account = Account(self.__client_id, currency)
            self.__accounts[currency] = new_account
            return f'Account with the {currency} successfuly created for {self.__first_name} {self.__second_name}, id: {self.__client_id};'
        else:
            return f'ERROR! Account with the {currency} is already exist for {self.__first_name} {self.__second_name}, id: {self.__client_id};'

    def close_account(self, currency):
        if currency in self.__accounts:
            del self.__accounts[currency]
            return f'Account with the {currency} successfuly deleted from {self.__first_name} {self.__second_name}, id: {self.__client_id};'
        else:
            return f"\033[31mERROR! Account with the {currency} doesn't exist for {self.__first_name} {self.__second_name}, id: {self.__client_id};\033[0m"

    def transfer_btw_accounts(self, currency_from, currency_to, value):
        if currency_from not in self.__accounts:
            return f'ERROR! Account {currency_from} does not exist.'
        if currency_to not in self.__accounts:
            return f'ERROR! Account {currency_to} does not exist.'
        if currency_from == currency_to:
            return "ERROR! Cannot transfer to the same currency."

        result = self.__accounts[currency_from].withdraw(value)
        if "ERROR" in str(result):
            return result

        try:
            rate = EXCHANGE_RATES[currency_from][currency_to]
        except KeyError:
            return f"ERROR! No exchange rate for {currency_from} → {currency_to}"

        converted = value * rate
        self.__accounts[currency_to].deposit(converted)

        return (f'Transfer successful: {value:.2f} {currency_from} → '
                f'{converted:.2f} {currency_to} (rate {rate})')

    def export_statement(self, filename=None):
        if filename is None:
            filename = f"statement_{self.__first_name}_{self.__second_name}_{self.__client_id}.txt"

        total_byn = 0
        with open(filename, "w", encoding="utf-8") as f:
            f.write(
                f"Выписка по счетам клиента {self.__first_name} {self.__second_name}\n"
            )
            f.write(f"ID клиента: {self.__client_id}\n\n")
            for currency, acc in self.__accounts.items():
                balance = acc.get_balance()
                if "BYN" in EXCHANGE_RATES[currency]:
                    balance_byn = balance * EXCHANGE_RATES[currency]["BYN"]
                else:
                    balance_byn = 0
                total_byn += balance_byn
                f.write(
                    f"Счёт {currency}: {balance:.2f} {currency} ({balance_byn:.2f} BYN)\n"
                )

            f.write("\n")
            f.write(f"Суммарный баланс во всех валютах: {total_byn:.2f} BYN\n")

        return f"Statement saved to {filename}"

    def get_first_name(self):
        return self.__first_name

    def get_second_name(self):
        return self.__second_name

    def get_client_id(self):
        return self.__client_id

    def get_accounts(self):
        return self.__accounts

    def set_first_name(self, value):
        if value:
            self.__first_name = value

    def set_second_name(self, value):
        if value:
            self.__second_name = value


class Account:
    def __init__(self, client_id, currency):
        self.__client_id = client_id
        self.__currency = currency
        self.__balance = 0
        self.__account_id = uuid.uuid4()

    def deposit(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__balance += float(value)
            return f'Deposited {value} {self.__currency}'
        return 'ERROR! Incorrect value.'

    def withdraw(self, value):
        if isinstance(value, (int, float)) and value > 0 and self.__balance >= value:
            self.__balance -= float(value)
            return f'Withdrawn {value} {self.__currency}'
        return 'ERROR! Incorrect value or insufficient funds.'

    def get_client_id(self):
        return self.__client_id

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance

    def get_account_id(self):
        return self.__account_id

    def set_balance(self, value):
        if value != None:
            self.__balance = value
