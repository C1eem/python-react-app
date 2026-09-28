from authx import AuthX, AuthXConfig
from src.core.config import settings

config = AuthXConfig()
config.JWT_ALGORITHM = settings.JWT_ALGORITHM
config.JWT_SECRET_KEY = settings.SECRET_KEY
config.JWT_ACCESS_TOKEN_EXPIRES = settings.access_expire
config.JWT_REFRESH_TOKEN_EXPIRES = settings.refresh_expire

security = AuthX(config=config)
