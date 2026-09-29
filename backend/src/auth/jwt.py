from authx import AuthX, AuthXConfig
from src.core.config import settings

config = AuthXConfig()
config.JWT_ALGORITHM = settings.JWT_ALGORITHM
config.JWT_SECRET_KEY = settings.SECRET_KEY
config.JWT_ACCESS_TOKEN_EXPIRES = settings.access_expire
config.JWT_REFRESH_TOKEN_EXPIRES = settings.refresh_expire
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_ACCESS_COOKIE_NAME = "access_token"
config.JWT_REFRESH_COOKIE_NAME = "refresh_token"
config.JWT_COOKIE_CSRF_PROTECT = False  # для MVP
config.JWT_COOKIE_SECURE = False  # True в проде (HTTPS)
config.JWT_COOKIE_SAMESITE = "lax"  # или "strict"

security = AuthX(config=config)
