from rest_framework.response import Response
from rest_framework.decorators import api_view

from goods.models import SuperCategory
from .serializers import SuperCategorySerializer

@api_view(['GET'])
def super_category(request):
    if request.method == 'GET':
        super_category = SuperCategory.objects.all()
        serializer = SuperCategorySerializer(super_category, many=True)
        return Response(serializer.data)
