# register
# - first name, last name, email, username, password 
# - generaten user account
# login
# - account number & password
# bank operations

# Initializing the system
import random

database = {}  # dictionary


def init():
    print("Welcome to Yung Bank")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("=== Login ===")

    account_number_from_user = input("Type in your account number \n")
    is_valid_account_number = account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = input("Type in your password \n")

        for accountNumber, user_details in database.items():
            if accountNumber == int(account_number_from_user):
                if user_details[3] == password:
                    bank_operation(user_details)

        print('Invalid account or password')
        login()
    else:
        init()


def account_number_validation(account_number):
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account number")
                return False
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Account number cannot be less or more than 10digit")
            return False

    else:
        print("Account number is a required field")
        return False


def register():
    print("=== Register ===")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("create a password for yourself \n")

    account_number = generation_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? "
                                "(1) deposit "
                                "(2) withdrawal "
                                "(3) complain "
                                "(4) Logout "
                                "(5) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        complain_operation()
    elif selected_option == 4:

        logout()
    elif selected_option == 5:

        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    withdraw = input("How much will you like to withdraw? \n")
    print("Take your Cash \n Thank you for banking with us")

    init()


def deposit_operation():
    deposit = input('How much would you like to deposit today? \n')
    print('Your deposit has been deposited \n Thank you for Banking with us')

    init()


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def complain_operation():
    complaint = input("What issue will you like to report? \n")
    print("Your Complaint has been received \n Thank you for contacting us")


def logout():
    login()


init()
