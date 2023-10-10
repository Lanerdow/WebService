from flask import Flask, jsonify, render_template, redirect
import calendar

app = Flask(__name__)


@app.route('/calendar/<int:year>/<int:month>', methods=['GET'])
def get_calendar(year, month):
    if month < 1 or month > 12:
        return jsonify({"error": "Month should be between 1 and 12"}), 400

    return jsonify({"calendar": calendar.month(year, month)})


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)