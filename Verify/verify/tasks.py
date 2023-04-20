import os
import requests
from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost:6379/0')

API_KEY = os.environ.get("API_KEY")
SMS_ENDPOINT = "https://api.sms.ir/v1/send/verify"


@app.task()
def send_code(mobile, verification_otp):
    data = {
        "mobile": mobile,
        "templateId": 100000,
        "parameters": [
            {
                "name": "Code",
                "value": verification_otp
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "text/plain",
        "x-api-key": API_KEY
    }
    response = requests.post(SMS_ENDPOINT, json=data, headers=headers)
    print(response.json())
