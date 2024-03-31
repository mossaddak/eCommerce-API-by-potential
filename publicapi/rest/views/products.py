from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.permissions import AllowAny

from productio.models import Product

from ..serializers.products import PublicProductSerializer


class PublicProductList(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PublicProductSerializer
    queryset = Product.objects.get_status_fair()


class PublicProductDetails(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PublicProductSerializer
    queryset = Product.objects.get_status_fair()
    lookup_field = "slug"
