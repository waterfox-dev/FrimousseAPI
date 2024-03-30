from rest_framework_simplejwt.authentication import JWTAuthentication

from database.models import User


class CustomJWTAuthentication(JWTAuthentication):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_model = User
        