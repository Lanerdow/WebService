from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calendar/<string:year>/<string:month>', methods=['GET'])
def get_calendar(year, month):
    api_url = 'http://localhost:8080/calendar/'+year+'/'+month

    try:
        response = requests.get(api_url)
    except:
        print(f"Error for the request")
        return render_template('error.html')
    else:
        if response.status_code == 200:
            data = response.json()
            print(data["calendar"])
            return render_template('calendar.html', year=year, month=month, calendar=data['calendar'])
        else:
            print(f"Error for the request with status code {response.status_code}")
            return render_template('error.html')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
