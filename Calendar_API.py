from flask import Flask, jsonify, render_template
import calendar

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calendar/<int:year>/<int:month>', methods=['GET'])
def get_calendar(year, month):
    if month < 1 or month > 12:
        return jsonify({"error": "Month should be between 1 and 12"}), 400

    return jsonify({"year": year, "month": month, "calendar": calendar.month(year, month)})


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
