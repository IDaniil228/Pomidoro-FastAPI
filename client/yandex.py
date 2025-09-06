from dataclasses import dataclass

from Schema import YandexUserDataSchema
from setting import Setting

import httpx

@dataclass
class YandexClient:
    setting: Setting
    async_client : httpx.AsyncClient

    async def get_user_data(self, code : str) -> YandexUserDataSchema:
        access_token = await self._get_user_access_token(code=code)
        print(access_token, "access_token")
        user_info = await self.async_client.get("https://login.yandex.ru/info?format=json",
                        headers={"Authorization" : f"OAuth {access_token}"})
        print(user_info.json(), "user_info")
        return YandexUserDataSchema(**user_info.json(), yandex_access_token=access_token)

    async def _get_user_access_token(self, code : str):
        data = {
            "code": code,
            "client_id": self.setting.YANDEX_CLIENT_ID,
            "client_secret": self.setting.YANDEX_CLIENT_SECRET,
            "grant_type": "authorization_code",
        }
        print(data, "data")
        response = await self.async_client.post(
                self.setting.YANDEX_TOKEN_URL,
                data=data,
                headers={
                "Content-Type": "application/x-www-form-urlencoded"
        })
        print(response, "response")
        return response.json()["access_token"]