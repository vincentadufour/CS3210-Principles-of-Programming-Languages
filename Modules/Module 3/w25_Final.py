from functools import wraps
import datetime, time

database = {}

# Decorators
user_permissions = {"admin": True, "user": False}

# Decorator 1: Authorization Decorator
# Purpose: Verifies if the user has permission to execute the function
# Usage: Applied to functions where restricted access is required
def authorization_decorator(func):
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_permissions.get(user_role, False):  # Checks if the user_role is permitted
            return func(user_role, *args, **kwargs)
        else:
            print("Unauthorized access. Permission denied.")
            return None
    return wrapper

# Decorator 2: Logging Decorator
# Purpose: Keeps a log of when functions begin and end.
# Usage: Can be used for debugging, or any other scenario where a log of which functions are executed
# Usage: and when is required.
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG]{datetime.datetime.now()}: Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG]{datetime.datetime.now()}: Finished executing {func.__name__}")
        return result
    return wrapper

# Decorator 3: Validation Decorator
# Purpose: Acts as an input validator.
# Usage: Should be used on functions require specific parameters, in this case, requires at least 3 parameters,
# Usage: the last two of which must be integers.
def validation_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 3:  # Ensure at least three arguments (user_role, x, y) are provided
            print("Invalid inputs. Please provide a user role, and two integers.")
            return None
        
        user_role, x, y = args[:3]
        if isinstance(x, int) and isinstance(y, int):  # Validate if x and y are integers
            return func(*args, **kwargs)
        else:
            print("Invalid inputs. Please provide integers.")
            return None
    return wrapper

# Decorator 4: Timing Decorator
# Purpose: Records how long it takes for a function to complete.
# Usage: Can be used whenever a function's time efficiency is required.
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

# Functions

# Function 1: get_data
# Purpose: Retrieves the current state of the database
# Decorators Applied (with Order of Calling): authorization_decorator
@authorization_decorator  
def get_data(user_role):
    print(f"Accessed by: {user_role}")
    return database

# Function 2: update_data
# Purpose: Updates the database with new parameters
# Decorators Applied (with Order of Calling): log_decorator, authorization_decorator, timing_decorator, validation_decorator
@log_decorator 
@authorization_decorator 
@timing_decorator  
@validation_decorator  
def update_data(user_role, x, y):
    database[x] = y  # Updates the database
    print("Database updated successfully.")
    return database

# Function 3: delete_data
# Purpose: Removes a key:value pair from the database.
# Decorators Applied (with Order of Calling): log_decorator, authorization_decorator, timing_decorator
@log_decorator  
@authorization_decorator  
@timing_decorator  
def delete_data(user_role, key):
    print(user_role)
    if key in database:
        del database[key]
        print(f"'{key}' deleted from the database.")
    else:
        print(f"'{key}' not found in the database.")

# Testing the Functions
print(get_data("admin")) # Test for if the "admin" database is empty, Expected results: empty dictionary
print("\n")

update_data("admin", 10, 20)  # Test for updating admin database, Expected results: successful update with log and timing prints
print("\n")

update_data("admin", 10, 40)  # Test for updating admin database, Expected results: successful update with log and timing prints
print("\n")

update_data("admin", "ten", 20)  # Test for input validation, Expected results: invalid input error print, with log and timing prints
print("\n")

print(get_data("admin"))  # Test for verifying if "admin" database exists, Expected results: current values in database, {10: 40}
print("\n")

delete_data("admin", 10) #Test for deleting the key:value pair with key "10", Expected results: successful deletion with deletion, log, and timing prints
print("\n")

print(get_data("admin")) #Test for if the "admin" database is empty, Expected results: empty dictionary
print("\n")


update_data("user", 5, 10)  # Test for if validation decorator is working, Expected results: Access denied print, as well as log and timing prints
