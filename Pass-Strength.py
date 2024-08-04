import re

def check_password_strength(password):
    """
    Check the strength of a password based on several criteria.
    
    :param password: The password to check.
    :return: A string message about the strength of the password.
    """
    
    min_length = 8
    max_length = 20
    
   
    if len(password) < min_length:
        return "Password is too short. It should be at least 8 characters."
    if len(password) > max_length:
        return "Password is too long. It should be no more than 20 characters."
    
   
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    
  
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."

    if not re.search(r'[0-9]', password):
        return "Password should contain at least one digit."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character."
    
    return "Password is strong."


if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)
