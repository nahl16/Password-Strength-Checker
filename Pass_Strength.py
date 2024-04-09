def assess_password_strength(password):
    # Initialize criteria flags
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Calculate the number of fulfilled criteria
    criteria_count = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    # Determine password strength based on fulfilled criteria
    if criteria_count == 5:
        return "Very Strong"
    elif criteria_count >= 3:
        return "Strong"
    elif criteria_count >= 2:
        return "Moderate"
    elif criteria_count >= 1:
        return "Weak"
    else:
        return "Very Weak"

# Main program to prompt user for a password and assess its strength
if __name__ == "__main__":
    user_password = input("Enter your password: ")

    # Assess password strength
    strength = assess_password_strength(user_password)

    # Provide feedback to the user
    print(f"Password strength: {strength}")
