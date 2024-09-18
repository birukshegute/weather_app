from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    error_message = None
    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        try:
            data = get_weather(city, country)
        except KeyError:
            error_message = "No location was found based on your request."
    return render_template('index.html', data=data, error_message=error_message)

@app.route('/about')
def about():
    return render_template('about.html')

# if __name__ == '__main__':
#     app.run(debug=True)
