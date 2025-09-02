from dataclasses import dataclass

from Schema import GoogleUserDataSchema, YandexUserDataSchema
from setting import Setting

import requests

@dataclass
class YandexClient:
    setting: Setting

    def get_user_data(self, code : str) -> YandexUserDataSchema:
        access_token = self._get_user_access_token(code=code)
        user_info = requests.get("https://login.yandex.ru/info?format=json",
                                 headers={"Authorization" : f"OAuth {access_token}"})
        print(user_info.json(), "user_info")
        return YandexUserDataSchema(**user_info.json(), yandex_access_token=access_token)

    def _get_user_access_token(self, code : str):
        data = {
            "code": code,
            "client_id": self.setting.YANDEX_CLIENT_ID,
            "client_secret": self.setting.YANDEX_CLIENT_SECRET,
            "grant_type": "authorization_code",
        }
        response = requests.post(self.setting.YANDEX_TOKEN_URL, data=data, headers={
            "Content-Type": "application/x-www-form-urlencoded"
        })
        return response.json()["access_token"]