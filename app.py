from flask import Flask, jsonify, request
from db_utils import get_tour_dates

app = Flask(__name__)



@app.route('/tours/<date>')
def get_bookings(date):
    res = get_tour_dates(date)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True,  port=5001)
