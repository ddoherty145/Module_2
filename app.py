from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo.html')

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    
    context = {
        'flavor': users_froyo_flavor,
        'toppings': users_froyo_toppings
    }

    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')

@app.route('/favorites_results')
def favorites_results():
    animal = request.args.get('animal')
    color = request.args.get('color')
    city = request.args.get('city')
    return render_template('favorites_results.html', color=color, animal=animal, city=city)

@app.route('/secret_message')
def secret_message():
    return render_template('secret_message.html')

@app.route('/message_results', methods=['POST'])
def message_results():
    message = request.form.get('message', '')
    sorted_message = ''.join(sorted(message))
    return render_template('message_results.html', sorted_message=sorted_message)


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    operand1 = int(request.args.get('operand1', 0))
    operand2 = int(request.args.get('operand2', 0))
    operation = request.args.get('operation')

    if operation == 'add':
        result = operand1 + operand2
        operation_text = 'add'
    elif operation == 'subtract':
        result = operand1 - operand2
        operation_text = 'subtract'
    elif operation == 'multiply':
        result = operand1 * operand2
        operation_text = 'multiply'
    elif operation == 'divide':
        if operand2 != 0:
            result = operand1 / operand2
        else:
            result = 'undefined (division by zero)'
        operation_text = 'divide'
    else:
        result = 'invalid operation'
        operation_text = 'invalid'

    return render_template('calculator_results.html', operand1=operand1, operand2=operand2, operation_text=operation_text, result=result)

        
HOROSCOPE_PERSONALITIES = {
    "aries": "Adventurous and energetic",
    "taurus": "Patient and reliable",
    "gemini": "Witty and outgoing",
    "cancer": "Caring and protective",
    "leo": "Confident and ambitious",
    "virgo": "Practical and diligent",
    "libra": "Charming and diplomatic",
    "scorpio": "Passionate and resourceful",
    "sagittarius": "Optimistic and freedom-loving",
    "capricorn": "Disciplined and responsible",
    "aquarius": "Innovative and unique",
    "pisces": "Compassionate and artistic"
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')
    personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign, "an interesting and unique individual.")
    random.seed(1 if horoscope_sign == 'aries' else 3 if horoscope_sign == 'taurus' else None)
    lucky_number = random.randint(1, 99)

    return render_template('horoscope_results.html', users_name=users_name, horoscope_sign=horoscope_sign, personality=personality, lucky_number=lucky_number)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
