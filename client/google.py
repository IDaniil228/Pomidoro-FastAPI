from dataclasses import dataclass

from Schema import GoogleUserDataSchema
from setting import Setting

import httpx

@dataclass
class GoogleClient:
    setting: Setting
    async_client : httpx.AsyncClient

    async def get_user_data(self, code : str) -> GoogleUserDataSchema:
        access_token = await self._get_user_access_token(code=code)
        print(access_token, "access_token")
        user_info = await self.async_client.get("https://www.googleapis.com/oauth2/v1/userinfo",
                                     headers={"Authorization" : f"Bearer {access_token}"})
        return GoogleUserDataSchema(**user_info.json(), google_access_token=access_token)

    async def _get_user_access_token(self, code : str):
        data = {
            "code": code,
            "client_id": self.setting.GOOGLE_CLIENT_ID,
            "client_secret": self.setting.GOOGLE_CLIENT_SECRET,
            "redirect_uri": self.setting.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
            #"redirect_uri": "http://127.0.0.1:8000/auth/google",
        }
        response = await self.async_client.post(self.setting.GOOGLE_TOKEN_URL, data=data)
        return response.json()["access_token"]