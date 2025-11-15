from bank import Bank
import uuid

b = Bank("МегаДеньгиБанк")


def main_menu():
    while True:
        print(f"\n========== {b.get_name()} ==========")
        print("1. Create Client")
        print("2. List Of Clients")
        print("3. Operations With Client (by ID)")
        print("4. Exit")

        choice = input("Enter choice: ")
        match choice:
            case "1":
                create_client()
            case "2":
                list_clients()
            case "3":
                client_operations()
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")


def create_client():
    print("\n===== CREATE NEW CLIENT =====")
    first = input("First Name: ")
    last = input("Second Name: ")
    client = b.create_client(first, last)
    print(f"Client created! ID: {client.get_client_id()}")


def list_clients():
    print("\n===== LIST OF CLIENTS =====")
    if not b.get_clients():
        print("No clients yet.")
        return
    for cid, client in b.get_clients().items():
        print(f"{cid} | {client.get_first_name()} {client.get_second_name()} | Accounts: {list(client.get_accounts().keys())}")


def client_operations():
    client_id = input("Enter client ID: ")
    if client_id not in map(str, b.get_clients().keys()):
        print("Client not found.")
        return

    client = b.get_clients()[uuid.UUID(client_id)]
    while True:
        print(
            f"\n===== {client.get_first_name()} {client.get_second_name()} =====")
        print("1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Between Accounts")
        print("5. Close Account")
        print("6. Show Balances")
        print("7. Write info in file")
        print("8. Back")
        choice = input("Enter choice: ")
        match choice:
            case "1":
                currency = input("Currency: ").upper()
                print(client.open_account(currency))
            case "2":
                currency = input("Currency: ").upper()
                value = float(input("Amount: "))
                if currency in client.get_accounts():
                    print(client.get_accounts()[currency].deposit(value))
                else:
                    print("No such account.")
            case "3":
                currency = input("Currency: ").upper()
                value = float(input("Amount: "))
                if currency in client.get_accounts():
                    print(client.get_accounts()[currency].withdraw(value))
                else:
                    print("No such account.")
            case "4":
                c_from = input("From currency: ").upper()
                c_to = input("To currency: ").upper()
                value = float(input("Amount: "))
                print(client.transfer_btw_accounts(c_from, c_to, value))
            case "5":
                currency = input("Currency: ").upper()
                print(client.close_account(currency))
            case "6":
                print("\n===== ACCOUNTS & BALANCES =====")
                accounts = client.get_accounts()
                if not accounts:
                    print("No accounts yet.")
                else:
                    for acc in accounts.values():
                        print(
                            f"Account ID: {acc.get_account_id()} | Currency: {acc.get_currency()} | Balance: {acc.get_balance()}")
            case "7":
                print(client.export_statement())
            case "8":
                break
            case _:
                print("Invalid option!")


if __name__ == "__main__":
    main_menu()
