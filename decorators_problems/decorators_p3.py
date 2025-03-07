# Access Control Decorator
#
# Problem Statement:
#
# Create a decorator @requires_role(role) that:
#
# Restricts access to a function based on the user's role.
#
# If the role matches, the function executes normally.
#
# If the role does not match, it raises a PermissionError.
#
# Example:
#
# @requires_role("admin")
#
#
# def delete_user():
#
#
#   print("User deleted")
#
#
# Calling delete_user() should only work for admin users.


def requires_role(required_role):
    def decorator(func):
        def wrapper(user_role):
            if user_role==required_role:
                return func()  # Call the function normally
            else:
                raise PermissionError(f"Access denied: '{user_role}' role cannot perform this action.")
        return wrapper
    return decorator

@requires_role("admin")  # Only "admin" can call this function
def delete_user():
    print("User deleted successfully.")

try:
    delete_user("admin")
except PermissionError as e:
    print(e)




