def check_password_strength(password):
    # Your password strength checking logic here
    # Return a message indicating the strength
    return "Strong" if len(password) >= 8 else "Weak"

def test_password_strength_checker():
    password = "securepassword"
    result = check_password_strength(password)
    print(f"Password: {password} - Strength: {result}")
   