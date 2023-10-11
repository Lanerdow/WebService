from flask import Flask, jsonify
import calendar

app = Flask(__name__)


@app.route('/calendar/<int:year>/<int:month>', methods=['GET'])
def get_calendar(year, month):
    if month < 1 or month > 12:
        return jsonify({"error": "Month should be between 1 and 12"}), 400
    text_cal = calendar.HTMLCalendar(firstweekday=0)

    # default value of width is 0

    # printing formatmonth
    print(text_cal.formatmonth(year, month))
    print(str(calendar.month(year, month)))
    return jsonify({"calendar": text_cal.formatmonth(year, month)})
    #return calendar.month(year, month)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)