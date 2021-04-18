# Budget APP
# Create new category
# Withdrawing funds from each category
# Depositing funds to each of the categories
# Computing category balances
# Transferring balance amounts between categories


database = dict()


class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount, bal):
        bal += amount
        return bal

    def withdraw(self, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        """
Computing category balances
        """
        for category, bal in db.items():
            print(category, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db


def init() -> object:
    print("===Welcome to the Budget App=== \n")
    menu()


def menu():
    try:

        user = int(
            input(
                '\n ===What would you like to do?=== \n '
                'Press (1) To create a new budget \n '
                'Press (2) To deposit into budget \n '
                'Press (3) To withdraw from budget \n '
                'Press (4) To check budget balance \n '
                'Press (5) To transfer budget balance \n '
                'Press (6) To exit\n'
            )
        )
    except:
        print("Invalid Selection")
        menu()

    if user == 1:
        create_new_budget()
    elif user == 2:
        deposit()
    elif user == 3:
        withdraw()
    elif user == 4:
        balance()
    elif user == 5:
        transfer()
    elif user == 6:
        exit()
    else:
        print("Invalid selection")
        menu()


def create_new_budget():
    print("\n=== Creating New Budget === \n")

    budget_title = input("Enter budget name \n")
    try:
        amount = int(input("Enter your budget amount \n$"))
    except:
        print("\n Invalid input")
        create_new_budget()
    budget = Budget(budget_title, amount)
    database[budget_title] = amount
    print("")
    print(f'Budget {budget_title} was setup with ${amount}')
    menu()


def withdraw():
    print("=== Withdraw from a created budget ===\n")
    print("=== Available Budget ===")

    for key, value in database.items():
        print(f"-  {key}")

    pick = int(
        input("\nPress (1) To continue with your withdrawal transaction \n "
              "Press (2) To stop withdrawal transaction\n")
    )
    if pick == 1:
        user = input(
            "\n === Select one of the budget mentioned above ===\n"
        )
        if user in database:
            print("PS: You can not withdraw all your budget funds, $1 must remain")
            amt = int(
                input("Enter amount \n$")
            )
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.withdraw(user, amt, balance)
                database[user] = new_balance
                print(f"${amt} has been withdrawn from the Budget-{user}"
                      f"\nBudget amount remaining ${new_balance}")
                menu()

            else:
                pick = int(
                    input(
                        f"\nBudget {user} is insufficient of the ${amt} required"
                        f"\n The actual balance {database[user]}\nPress (1) To deposit \n Press (2) to continue"
                    )
                )
                if pick == 1:
                    amt = int(input("Enter amount \n$"))
                    balance = int(database[user])
                    new_balance = Budget.deposit(amt, balance)
                    database[user] = new_balance
                    print("")
                    print(f"Budget {user} has been credited with ${amt}\n")
                    withdraw()
                elif pick == 2:
                    withdraw()
                else:
                    print("Invalid option\n")
                    withdraw()
        else:
            pick = int(
                input(
                    f"\n === Budget {user} does not exist! ====\n "
                    f"Press (1) To create a new budget\n"
                    f"Press (2) To choose the existing Budget\n"
                    f"Press (3) To go to back to menu\n"
                )
            )
            if pick == 1:
                create_new_budget()
            elif pick == 2:
                withdraw()
            elif pick == 3:
                print("")
                menu()
            else:
                print("Invalid option\n")
                withdraw()
    elif pick == 2:
        print("\nYou have terminated the withdrawal transaction")
        menu()
    else:
        print("\nInvalid option")
        withdraw()


def deposit():
    print("=== Deposit into a budget ===\n")
    print("=== Available Budget ===")
    for key, value in database.items():
        print(f"-  {key}")

    pick = int(
        input("\nPress (1) To continue with your deposit transaction\n"
              "Press (2) To stop deposit transaction\n")
    )
    if pick == 1:
        user = input("Select a budget \n")
        if user in database:
            amt = int(input("Enter amount \n$"))
            bal = int(database[user])
            new_balance = Budget.deposit(amt, bal)
            database[user] = new_balance
            print(f"\nBudget {user} is credited with ${amt}\n"
                  f"Total Budget amount is now ${new_balance}")
            menu()

        else:
            print("")
            pick = int(
                input(
                    f"Budget {user} does not exist!\n"
                    f"Press (1) To create a new budget\n"
                    f"Press (2) To choose the right budget\n"
                    f"Press (3) To go back to menu\n"
                )
            )
            if pick == 1:
                create_new_budget()
            elif pick == 2:
                deposit()
            elif pick == 3:
                menu()
            else:
                print("Invalid option\n")
                deposit()

    elif pick == 2:
        print("\nYou terminated the deposit transaction")
        menu()
    else:
        print("\ninvalid transaction")
        deposit()


# Computing category balances
def balance():
    print("=== Gettig your Budget Balance ===\n")
    check_bal = Budget.balance(database)
    if (check_bal == None):
        print("")
        menu()
    else:
        print(f"${check_bal}")
        menu()


def transfer():
    print("=== Available and Valid Budget ===")
    for key, value in database.items():
        print(key)
        print("")
    print("==== Transfer Operation ===")
    print('Note: You can not withdraw all your budget, at least $1 must remain.\n')
    from_budget = input("Enter the bugdet you are transfering from\n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to transfer\n$"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds\n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("")
                print(f"You have successful transferred ${from_amount} from {from_budget} to {to_budget}")
                for key, value in db.items():
                    print(key, value)
                menu()
            else:
                print(f"\n{from_budget} Budget does not exist, please choose from the valid budget below\n")
                transfer()
        else:
            print(f"You do not have such amount -${from_amount} in {from_budget}")
            transfer()
    else:
        print(f"Budget {from_budget} does not exist\n")
        transfer()


def exit():
    global pick
    try:
        pick = int(input("Are you sure you want to quit?\n"
                         "Press (1) to quit\n"
                         "Press (2) to continue\n"))
    except:
        print("Invalid input\n")
        exit()

    if pick == 1:
        print("\nWe hope yo had a good budgeting setup, bye for now.\n")
        quit()
    elif pick == 2:
        menu()
    else:
        print("Invalid input\n")
        exit()


init()
