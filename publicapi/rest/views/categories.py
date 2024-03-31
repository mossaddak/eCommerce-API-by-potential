from rest_framework.generics import ListAPIView, RetrieveAPIView

from common.permissions import IsSeller

from productio.models import Category
from productio.rest.serializers.categories import CatrgorySerializer


class PublicProductCategoryList(ListAPIView):
    permission_classes = [IsSeller]
    serializer_class = CatrgorySerializer
    queryset = Category.objects.all()
