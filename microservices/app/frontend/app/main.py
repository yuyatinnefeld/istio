from flask import Flask, render_template, request, jsonify

import json
import requests
import time
from concurrent.futures import ThreadPoolExecutor
import os

# Read environment variables
version = os.getenv("VERSION", "0.0.0")
env = os.getenv("ENV", "ENV_NOT_DEFINED")
pod_id = os.getenv("VERSION", "PODID_NOT_DEFINED")
platform = os.getenv("PLATFORM", "LOCAL")

app = Flask(__name__)


def check_status(url):
    try:
        return requests.get(url, headers={'Content-Type': 'application/json'})
    except Exception as exc:
        print("ERROR: check_status")
        return {"status":"error", "message": "status != 200 | service not available"}
    

def serialize_data(response):
    try:
        response_text = response.text
        if "details" in response_text:
            data = response_text.replace("\"", "\'")
        else:
            data = response.json()
    except Exception as exc:
        error_message =  '{ "status":"error", "message": "data cannot be serialized" }'
        data = json.loads(error_message)
        print("ERROR: serialize_data")
    return data


def get_url(service_name, port):
    if platform == "K8S":
        url = f'http://{service_name}-service:{port}'
    elif platform == "LOCAL":
        url = f'http://localhost:{port}'
    else:
        url = "service is not available"
    
    print("URL: ", url)
    return url


def fetch_url(url):
    response = check_status(url)
        
    try:
        status = response.status_code
        if status == 200:
            print(f"SUCCESS: URL={url}, status == 200")
    except Exception as exc:
            print(f"ERROR: URL={url}, status != 200")
            return {"status":"error", "message": "status != 200 | service not available"}
    
    result_data = serialize_data(response)
    return result_data


@app.route('/health', methods=['GET'])
def health():
    return jsonify("Frontend APP is healthy")


@app.route('/login')
def login():
    user_name = request.headers.get('end-user', 'Unknown User')
    return render_template('index.html', user_name=user_name)


@app.route('/set_end_user', methods=['POST'])
def set_end_user():
    time.sleep(3)
    user_name = request.form.get('user_name')    
    url = get_url('reviews', '9999')
    
    if url == "service is not available":
        reviews_data = "local dummy reviews data"
    else:
        with ThreadPoolExecutor() as executor:
            reviews_data = list(executor.map(fetch_url, [url]))[0]

    message = f"response.headers['end-user'] = {user_name} | REVIEWS API: {reviews_data}"
    response = jsonify(message)
    response.headers['end-user'] = user_name
    return response


@app.route('/', methods=['GET'])
def index():
    details_url = get_url('details', '7777')
    payment_url = get_url('payment', '8888')
    reviews_url = get_url('reviews', '9999')
    
    url_list = [details_url, payment_url, reviews_url]
    
    with ThreadPoolExecutor() as executor:
        result_data_list = list(executor.map(fetch_url, url_list))
    
    frontend_api_info=f"FRONTEND API: {version} | env: {env} | pod_id: {pod_id} | platform: {platform}"
    
    result = jsonify(
        api=frontend_api_info,
        details=result_data_list[0],
        payment=result_data_list[1],
        reviews=result_data_list[2],
    )

    return result


if __name__ == '__main__':
    app.run(debug=True)

