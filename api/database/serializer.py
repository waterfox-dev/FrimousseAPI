from rest_framework.serializers import ModelSerializer

from database.models import Company


class CompanySerializer(ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'
        
        