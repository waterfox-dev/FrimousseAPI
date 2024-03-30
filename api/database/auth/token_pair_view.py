from rest_framework_simplejwt.views import TokenObtainPairView

from database.auth.token_serializer import CustomTokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairView):
    
    serializer_class = CustomTokenObtainPairSerializer
    
    