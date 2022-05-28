import time

import requests

from not_service.settings import TOKEN, URL


def send_message(content: list, text):
    bearer_token = TOKEN
    for item in content:
        time.sleep(5)
        url = f"{URL}/{item['id']}"
        json = item
        json['text'] = text
        response = requests.post(url=url,
                                 json=json,
                                 headers={"Authorization": "Bearer " + bearer_token})
        print(f"Сообщение '{text}' на номер {json['phone_number']} отправлено, {response.json()}")
    return response.json()
