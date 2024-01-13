from flask import Flask, render_template, request, jsonify

import json
import requests


app = Flask(__name__)

def fetch_data(url):

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Status: 200")
    except Exception as exc:
        error_message =  '{ "status":"erro", "message": "status != 200" }'
        data = json.loads(error_message)

    try:
        print("Serialize Data to Json")
        response_text = response.text
        print("Response: ", response_text)
        
        if "details" in response_text:
            data = response_text.replace("\"", "\'")
        else:
            data = response.json()
    except Exception as exc:
        print(exc)
        error_message =  '{ "status":"error", "message": "data cannot be serialized" }'
        data = json.loads(error_message)
        is_serialized = False
    return data
        

@app.route('/test', methods=['GET'])
def test():
    message = f"Frontend APP - TEST PAGE"
    return jsonify(message)


@app.route('/login')
def login():
    user_name = request.headers.get('end-user', 'Unknown User')
    return render_template('index.html', user_name=user_name)


@app.route('/set_end_user', methods=['POST'])
def set_end_user():
    user_name = request.form.get('user_name')

    # CHECK HERE WITCH MODE YOU WANT TO HAVE!
    is_api_from = "k8s"
    frontend_version = "1.0.0"
    
    try:
        if is_api_from == "k8s":
            reviews_data = fetch_data('http://reviews-service:9999')
        else:
            reviews_data = "local reviews data"

        message = f"USER: {user_name} | FRONTEND API: {frontend_version} - REVIEWS API: {reviews_data}"
        return jsonify(message)

    except Exception as exc:
        print(exc)
        return jsonify({'error': 'Failed to fetch data from backend APIs', 'message': exc}), 5000

@app.route('/', methods=['GET'])
def index():
    # CHECK HERE WITCH MODE YOU WANT TO HAVE!
    is_api_from = "k8s"
    frontend_version = "1.0.0"
    
    try:
        if is_api_from == "k8s":
             # fetch data from kubernetes services #
            reviews_data = fetch_data('http://reviews-service:9999')
            payment_data = fetch_data('http://payment-service:8888')
            details_data = fetch_data('http://details-service:7777') 
        
        elif is_api_from == "docker":
            #!!!! fetch data from public apis !!!!#
            reviews_data = fetch_data('http://testing-yuya.com/reviews')
            payment_data = fetch_data('http://testing-yuya.com/payment')
            details_data = fetch_data('http://testing-yuya.com/details')
            
        else:
            reviews_data = "dummy reviews data"
            payment_data = "dummy payment data"
            details_data = "dummy details data"

        message = f"FRONTEND API: {frontend_version} - REVIEWS API: {reviews_data}, PAYMENT API: {payment_data}, DETAILS API: {details_data}"
        return jsonify(message)

    except Exception as exc:
        print(exc)
        return jsonify({'error': 'Failed to fetch data from backend APIs', 'message': exc}), 5000

if __name__ == '__main__':
    app.run(debug=True)