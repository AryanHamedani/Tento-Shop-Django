from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tento_shop_project.products.models import Product

from .serializers import ProductListSerializer


@api_view(["POST"])
def search(request):
    query = request.data.get("query", "")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
