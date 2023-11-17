import requests
import random
from django.conf import settings


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(1000,9999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}'

        response = requests.get(url)

        hedders = response.headers

        content = response.content

        print(f'this is data ==== {hedders}')

        print(f'this is data ==== {content}')

        return otp

    except Exception as e:
        print(f'An error occurred:{e}')
        return None
    