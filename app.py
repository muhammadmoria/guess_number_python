from flask import Flask, request, render_template
import random

app = Flask(__name__)

random_number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        guess = int(request.form['guess'])
        message = check_guess(guess)
    return render_template('index.html', message=message)

def check_guess(guess):
    if guess == random_number:
        return f"Congratulations! You've guessed the number {random_number} correctly!"
    elif guess < random_number:
        return "Too low! Try a higher number."
    else:
        return "Too high! Try a lower number."

if __name__ == '__main__':
    app.run(debug=True)
