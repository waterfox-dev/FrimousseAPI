from rest_framework.viewsets import ModelViewSet

from database.models import Company
from database.serializer import CompanySerializer


class CompanyViewset(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        return Company.objects.filter(status=True)