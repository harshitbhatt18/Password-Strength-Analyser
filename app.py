import re
import string
import random
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

class PasswordStrengthTester:
    def __init__(self, dictionary_file):
        self.common_passwords = self.load_common_passwords(dictionary_file)

    def load_common_passwords(self, dictionary_file):
        with open(dictionary_file, "r") as file:
            common_passwords = [line.strip() for line in file]
        return common_passwords

    def test_password(self, password):
        score = 0
        feedback = []    
        
        if password.lower() in self.common_passwords:
            feedback.append("Password is too common. Avoid using common passwords.")
        else:
            score += 1
            
        #length score
        length = len(password)
        if length < 6:
            feedback.append("Password is too short. Minimum length is 6 characters.")
        elif length <= 8:
            score += 1
            feedback.append("Password length is acceptable but could be longer.")
        elif length <= 10:
            score += 2
            feedback.append("Password length is good.")
        else:
            score += 3
            feedback.append("Password length is excellent.")

        # Complexity score
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(c in string.punctuation for c in password)

        if lower and upper and digit and special:
            score += 4
            feedback.append(
                "Password has a good mix of lowercase, uppercase, digits, and special characters."
            )
        elif lower and upper and digit:
            score += 3
            feedback.append(
                "Password has lowercase, uppercase, and digits. Adding special characters would improve strength."
            )
        elif lower and upper:
            score += 2
            feedback.append(
                "Password has both lowercase and uppercase letters. Adding digits and special characters would improve strength."
            )
        elif lower and digit:
            score += 2
            feedback.append(
                "Password has both lowercase letters and digits. Adding uppercase and special characters would improve strength."
            )
        elif lower:
            score += 1
            feedback.append(
                "Password has only lowercase letters. Adding uppercase letters, digits, and special characters would significantly improve strength."
            )

        # Sequence score
        if re.search(r"(.)\1{2,}", password):
            feedback.append(
                "Password has sequences of repeated characters. Avoid using repeated sequences."
            )
        else:
            score += 1

        # strength level
        if score <= 3:
            strength_level = "Weak"
        elif score <= 5:
            strength_level = "Moderate"
        else:
            strength_level = "Strong"

        return {
            "password": password,
            "score": score,
            "strength": strength_level,
            "feedback": feedback,
        }

tester = PasswordStrengthTester("10k_most_common.txt")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form["password"]
        result = tester.test_password(password)
    return render_template("index.html", result=result)

@app.route("/generate_password", methods=["POST"])
def generate_password():
    data = request.json
    length = data.get("length", 16)
    user_charset = data.get("user_charset", "")
    default_charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    if len(user_charset) > length:
        return jsonify(error="The specified length is less than the number of characters to include."), 400

    password = list(user_charset)
    while len(password) < length:
        password.append(random.choice(default_charset))

    random.shuffle(password)
    return jsonify(password=''.join(password))

if __name__ == "__main__":
    app.run(debug=True)