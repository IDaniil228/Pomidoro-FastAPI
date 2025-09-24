from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_NAME : str = "hh"
    DB_HOST : str = "localhost"
    DB_PORT : int = 5432
    DB_USER : str = "hh"
    DB_PASSWORD : str = "1234"
    DB_DRIVER : str = "postgresql+asyncpg"

    CACHE_HOST : str = "localhost"
    CACHE_PORT : int = 6379
    CACHE_DB : int = 0

    JWT_SECRET_KEY : str = "secret_key"
    JWT_ALGORITHM : str = "HS256"

    GOOGLE_CLIENT_ID : str = "1003699936358-anqb0fba1g0j8tc9t1s8kk726v8nshjr.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET : str = "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"
    GOOGLE_REDIRECT_URI : str = "http://127.0.0.1:8000/auth/google"
    GOOGLE_TOKEN_URL : str = "https://accounts.google.com/o/oauth2/token"

    YANDEX_CLIENT_ID : str = "852927e0f58146a1a54b865a8269fbf1"
    YANDEX_CLIENT_SECRET : str = "a82adf3635874700aebf2d9634dc3af1"
    YANDEX_REDIRECT_URI : str = "http://localhost:8000/auth/yandex"
    YANDEX_TOKEN_URL : str = "https://oauth.yandex.ru/token"

    BROKER_URL : str = "amqp://guest:guest@localhost:5672"

    FROM_MAIL : str = "bukden12@gmail.com"
    SMTP_PORT : int = 465
    SMTP_HOST : str = "smtp.gmail.com"
    SMTP_PASSWORD : str = "eyhi nvwi hobe feyr"

    @property
    def db_url(self) -> str:
        return  f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def google_redirect_url(self) -> str:
        return f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"


    @property
    def yandex_redirect_url(self) -> str:
        return f"https://oauth.yandex.ru/authorize?response_type=code&client_id={self.YANDEX_CLIENT_ID}&redirect_uri={self.YANDEX_REDIRECT_URI}"