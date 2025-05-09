from functools import wraps
import time
import datetime




# Decorator 1
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG]{datetime.datetime.now()}: Executing{func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG]{datetime.datetime.now()}: Finished{func.__name__}")
        return result
    return wrapper




# Decorator 2
user_permissions = {"admin": True, "user": False}
def authorization_decorator(func):
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        if user_permissions.get(user_role, False):
            return func(user_role, *args, **kwargs)
        else:
            print("Unauthorized access. Permission denied.")
            return None
    return wrapper




# Decorator 3
def validation_dectorator(func):
	@wraps(func)
	def wrapper(x,y):
		if isinstance(x,int) and isinstance(y,int):
			return func(x,y)
		else:
			print("invalid inputs. Please provide integers.")
		return None
	return wrapper





# Decorator 4
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper






# main
database = {}


@logging_decorator
@authorization_decorator
def get_data():
    return database


@logging_decorator
@authorization_decorator
@timing_decorator
@validation_dectorator
def update_data(data):
    database.update(data)
    print("Database updated successfully.")
    return database


@logging_decorator
@authorization_decorator
@timing_decorator
def delete_data(key):
    if key in database:
        del database[key]
        print(f"'{key}' deleted from the database.")
    else:
        print(f"'{key}' not found in the database.")










# Test cases
print(get_data("admin"))

update_data("admin", 10, 20)  # Valid inputs
update_data("admin", "ten", 20)  # Invalid inputs (trigger validation decorator)

print(get_data("admin"))

delete_data("admin", "result")
print(get_data("admin"))

# Test unauthorized access
update_data("user", 5, 10)

