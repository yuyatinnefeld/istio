from flask import Flask, render_template, redirect, request, jsonify, session

import json
import requests


app = Flask(__name__)

def check_status(url):
    headers = {'Content-Type': 'application/json'}

    try:
        print("check response")
        response = requests.get(url, headers=headers)
    except Exception as exc:
        RuntimeError(exc)

    try:        
        if response.status_code == 200:
            print("status_code == 200")
            return response
        else:
            print(("status_code != 200"))
            return {"status":"error", "message":"status_code != 200"}
        
    except Exception as exc:
        RuntimeError(exc)


def serialize_data(response):
    print("serialize_data - data -> json")

    try:
        response_text = response.text
        print("Response: ", response_text)
        
        if "details" in response_text:
            data = response_text.replace("\"", "\'")
        else:
            data = response.json()
    except Exception as exc:
        print(exc)
        error_message =  '{ "status":"error", "message": "service is not available or data cannot be serialized" }'
        data = json.loads(error_message)
    return data


def get_url(env, service_name, port):
    if env == "k8s":
        url = f'http://{service_name}-service:{port}'
    elif env == "localhost":
        url = f'http://localhost:{port}'
    else:
        url = "service is not available"
    
    print(f"url: {url}")
    return url
            

@app.route('/health', methods=['GET'])
def health():
    return jsonify("Frontend APP is health")


@app.route('/login')
def login():
    user_name = request.headers.get('end-user', 'Unknown User')
    return render_template('index.html', user_name=user_name)


@app.route('/set_end_user', methods=['POST'])
def set_end_user():
    user_name = request.form.get('user_name')    
    url = get_url("k8s", 'reviews', '9999')
    
    if url == "service is not available":
        reviews_data = "local dummy reviews data"
    else:
        response = check_status(url)
        reviews_data = serialize_data(response)
    
    message = f"response.headers['end-user'] = {user_name} | REVIEWS API: {reviews_data}"
    response = jsonify(message)
    response.headers['end-user'] = user_name
    return response


@app.route('/', methods=['GET'])
def index():
    frontend_version = "2.0.0"
    env = "k8s"
    details_url = get_url(env, 'details', '7777')
    payment_url = get_url(env, 'payment', '8888')
    reviews_url = get_url(env, 'reviews', '9999')
    
    url_list = [details_url, payment_url, reviews_url]
    result_data_list = []
    
    for url in url_list:
        if url == "service is not available":
            result_data = "local dummy data"
        else:
            response = check_status(url)
            result_data = serialize_data(response)
        
        result_data_list.append(result_data)

    message = f"FRONTEND API: {frontend_version} - DETAILS API: {result_data_list[0]}, PAYMENT API: {result_data_list[1]}, REVIEWS API: {result_data_list[2]}"
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)