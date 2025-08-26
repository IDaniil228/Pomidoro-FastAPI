from dataclasses import dataclass

from Schema import GoogleUserDataSchema
from setting import Setting

import requests

@dataclass
class GoogleClient:
    setting: Setting

    def get_user_data(self, code : str) -> GoogleUserDataSchema:
        access_token = self._get_user_access_token(code=code)
        user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo",
                                 headers={"Authorization" : f"Bearer {access_token}"})
        return GoogleUserDataSchema(**user_info.json(), google_access_token=access_token)

    def _get_user_access_token(self, code : str):
        data = {
            "code": code,
            "client_id": self.setting.GOOGLE_CLIENT_ID,
            "client_secret": self.setting.GOOGLE_CLIENT_SECRET,
            "redirect_uri": "http://127.0.0.1:8000/auth/google",
            #"redirect_url": self.setting.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        response = requests.post(self.setting.GOOGLE_TOKEN_URL, data=data)
        print(f"Status: {response.status_code}")
        print(f"Response text: {response.text}")
        return response.json()["access_token"]