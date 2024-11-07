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
    return render_template('templates/froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    
    context = {
        'flavor': users_froyo_flavor,
        'topping': users_froyo_toppings
    }

    return render_template('templates/froyo_form.html', **context)

@app.route('/favorites')
def favorites():
    return """
    <form action="/favorites_results" method="GET">
        What is your Favorite Color?<br/>
        <input type="text" name="color"><br/>
        What is your Favorite Animal?<br/>
        <input type="text" name="animal"><br/>
        What is your Facortie City?<br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_fav_animal = request.args.get('animal')
    users_fav_color = request.args.get('color')
    users_fav_city = request.args.get('city')
    return f'Wow, I didn\'t know {users_fav_color} {users_fav_animal}s lived in {users_fav_city}!'

@app.route('/secret_message')
def secret_message():
    return """
    <form action="/message_results" method="POST">
        Enter your secret message:<br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit">
    </form>
    """
@app.route('/message_results', methods=['POST'])
def message_results():
    user_message = request.form.get('message', '')
    sorted_message = ''.join(sorted(user_message))
    return f'Heres your secret message: {sorted_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('templates/calculator_form.html')

@app.route('/calculator_results')
def calculator_results():

        operand1 = int(request.args.get('operand1', 0))
        operand2 = int(request.args.get('operand2', 0))
        operation = request.args.get('operation')

        if operation == "add":
            result = operand1 + operand2
            symbol = "+"
        elif operation == "subtract":
            result = operand1 - operand2
            symbol = "-"
        elif operation == "multiply":
            result = operand1 * operand2
            symbol = "*"
        elif operation == "divide":
            if operand2 != 0:
                result = operand1 / operand2
                symbol = "/"
            else:
                return "Error: Division by zero is not allowed."
        else:
         return "Invalid operation selected."
        
        context = {
            'operand1': operand1,
            'operand2': operand2,
            'symbol': symbol,
            'result': result
        }

        return render_template('templates/calculator_results.html', **context)




HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')

    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign, "an interesting and unique individual.")

    lucky_number = random.randint(1, 99)


    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
