# Student:    Vincent Dufour
# Professor:  Dr. Ranjidha Rajan
# Assignment: Homework 4: Generators
# Date:       13.04.2025
# Time Taken: Almost 2 hours


from functools import wraps
import datetime, time

user_permissions = {"admin": True, "user": False}

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG]{datetime.datetime.now()}: Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG]{datetime.datetime.now()}: Finished executing {func.__name__}")
        return result
    return wrapper


def authorization_decorator(func):
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_permissions.get(user_role, False):  # Checks if the user_role is permitted
            return func(*args, **kwargs)            # had to remove returning user role here so that check_balance didn't throw errors
        else:
            print("Unauthorized access. Permission denied.")
            return None
    return wrapper


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper


def validation_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # skipping validation if delete account is called since it only needs one argument
        if func.__name__ == "delete_account":
            return func(*args, **kwargs)


        if len(args) < 2:                   # had to bring this down to 2 in accordance with authorization decorator arguments
            print("Invalid inputs. Please provide an account number and an amount.")
            return None
        
        account_number, amount = args[:2]   # had to bring this down to 2 in accordance with authorization decorator arguments
        if isinstance(amount, int):
            return func(account_number, amount, **kwargs)
        else:
            print("Invalid input. Amount must be an integer.")
            return None
    return wrapper






# Initializing a simple database
atm_database = {}


@log_decorator
@authorization_decorator
def check_balance(account_number):
    return atm_database.get(account_number, "Account not found.")


@log_decorator
@authorization_decorator
@timing_decorator
@validation_decorator
def deposit(account_number, amount):
    if account_number in atm_database:
        atm_database[account_number] += amount
        print(f"Successfully deposited ${amount}. Current balance: ${atm_database[account_number]}")
    else:
        print("Account not found.")


@log_decorator
@authorization_decorator
@timing_decorator
@validation_decorator
def withdraw(account_number, amount):
    if account_number in atm_database:
        if atm_database[account_number] >= amount:
            atm_database[account_number] -= amount
            print(f"Successfully withdrew ${amount}. Current balance: ${atm_database[account_number]}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")


@log_decorator
@authorization_decorator
@timing_decorator
@validation_decorator
def delete_account(account_number):
    if account_number in atm_database:
        del atm_database[account_number]
        print(f"Account '{account_number}' deleted successfully.")
    else:
        print(f"'{account_number}' not found in the database.")




# Test cases
atm_database = {"123456": 1000, "654321": 500}  # Sample accounts

# Note: This also originally didn't work because the authorization decorator was
# returning user_role erroneously.
# Test for checking first user's balance. Expected output: "1000"
# as well as logging decorator output.
print("\nTest Case 1")
print(check_balance("admin", "123456"))

# Test for valid deposit for user 123456. Expected output: "Successfully deposited $200. Current balance: $1200"
# as well as logging and timing decorator outputs.
print("\nTest Case 2")
deposit("admin", "123456", 200)  # Valid deposit

# Test for wrong input type. Expected output: "Invalid inputs. Please provide integers."
# as well as logging and timing decorator outputs.
print("\nTest Case 3")
deposit("admin", "123456", "two hundred") 

# Test for successful withdrawal from available funds. Expected output: "Successfully withdrew $300. Current balance: $900"
# as well as logging and timing decorator outputs.
print("\nTest Case 4")
withdraw("admin", "123456", 300)  

# Test for overwithdrawal. Member does not have enough funds. Expected output: "Insufficient balance."
# as well as logging and timing decorator outputs.
print("\nTest Case 5")
withdraw("admin", "123456", 2000)  

# Test for successful balance check. Expected output: "900" 
# as well as logging decorator output.
print("\nTest Case 6")
print(check_balance("admin", "123456"))

# Test for successful account deletion Expected output: "Account '654321' deleted successfully."
# as well as logging and timing decorator outputs.
print("\nTest Case 7")
delete_account("admin", "654321")

# Test for checking balance on account that doesn't exist. Expected output: "Account not found."
# as well as logging decorator output.
print("\nTest Case 8")
print(check_balance("admin", "654321"))

# Test for user permissions. Expected output: "Unauthorized access. Permission denied."
# as well as logging and timing decorator outputs.
print("\nTest Case 9")
deposit("user", "123456", 100)
