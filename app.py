from flask import Flask, render_template, request
import random

app = Flask(__name__)

number = random.randint(1, 100)
attempts = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global number, attempts
    message = ""
    stars = ""

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])

            if guess < 1 or guess > 100:
                message = "Enter number between 1 and 100"
                return render_template("index.html", message=message, stars=stars)

            attempts += 1

            if guess == number:
                message = f"Correct! You win in {attempts} attempts!"

                if attempts <= 5:
                    stars = "⭐⭐⭐⭐⭐"
                elif attempts <= 8:
                    stars = "⭐⭐⭐⭐"
                elif attempts <= 10:
                    stars = "⭐⭐⭐"
                else:
                    stars = "⭐⭐"

                number = random.randint(1, 100)
                attempts = 0

            elif guess < number:
                message = "Too low!"
            else:
                message = "Too high!"

        except:
            message = "Invalid input"

    return render_template("index.html", message=message, stars=stars)

app.run(host='0.0.0.0', port=81)