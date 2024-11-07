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
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What are some Toppings you would Like?<br/>
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} with {users_froyo_toppings} on top!'

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
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

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

    
        return f"{operand1} {symbol} {operand2} = {result}"



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
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = ''

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = ''

    # TODO: Generate a random number from 1 to 99
    lucky_number = 0

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)