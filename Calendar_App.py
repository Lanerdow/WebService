from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calendar/<int:year>/<int:month>', methods=['GET'])
def get_calendar(year, month):
    api_url = 'http://localhost:5000/calendar/'+year+'/'+month

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print(f"Calendar for {data['year']} and the month {data['month']}:")
        print(data["calendar"])
        return render_template('calendar.html', year=data['year'], month=data['month'], calendar=data['calendar'])
    else:
        print(f"Error for the request with status code {response.status_code}")
        return response.status_code


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
