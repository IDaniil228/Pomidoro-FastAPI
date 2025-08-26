from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_NAME : str = "hh"
    DB_HOST : str = "localhost"
    DB_PORT : int = 5432
    DB_USER : str = "hh"
    DB_PASSWORD : str = "1234"
    DB_DRIVER : str = "postgresql+psycopg2"

    CACHE_HOST : str = "localhost"
    CACHE_PORT : int = 6379
    CACHE_DB : int = 0

    JWT_SECRET_KEY : str = "secret_key"
    JWT_ALGORITHM : str = "HS256"

    GOOGLE_CLIENT_ID : str = "1003699936358-anqb0fba1g0j8tc9t1s8kk726v8nshjr.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET : str = "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"
    GOOGLE_REDIRECT_URI : str = "http://127.0.0.1:8000/auth/google"
    GOOGLE_TOKEN_URL : str = "https://accounts.google.com/o/oauth2/token"

    @property
    def db_url(self):
        return  f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def google_redirect_url(self) -> str:
        return f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
