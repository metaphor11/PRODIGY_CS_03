import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    # Scoring
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~).")

    # Password strength evaluation
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    while True:
        print("\nPassword Strength Checker")
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        strength, feedback = check_password_strength(password)

        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for item in feedback:
                print(f" - {item}")

if __name__ == "__main__":
    main()
