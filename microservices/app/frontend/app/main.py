from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

def fetch_data(url):

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


@app.route('/test', methods=['GET'])
def test():
    message = f"Frontend APP - TEST PAGE"
    return jsonify(message)


@app.route('/', methods=['GET'])
def index():
    #!!!! fetch data from public apis !!!!#
    # review_data = fetch_data('http://testing-yuya.com/review')
    # payment_data = fetch_data('http://testing-yuya.com/payment')

    # fetch data from kubernetes services #
    review_data = fetch_data('http://review-service:9999')
    payment_data = fetch_data('http://payment-service:8888')
    
    if review_data is None or payment_data is None:
        return jsonify({'error': 'Failed to fetch data from backend APIs'}), 500
    else:
        message = f"Frontend APP - Review API: {review_data}, Payment API: {payment_data}"
        return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)