from rest_framework import serializers

from tento_shop_project.products import models


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Color
        fields = "__all__"


class SizeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SizeType
        fields = "__all__"


class SizeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SizeValue
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ProductImageGallery
#         fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField(read_only=True, many=True)
    category = serializers.StringRelatedField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    # price = serializers.SerializerMethodField(read_only=True)
    # colors = serializers.SerializerMethodField(read_only=True)
    absolute_url = serializers.SerializerMethodField(read_only=True)
    # rate = serializers.SerializerMethodField(read_only=True)
    # rate_count = serializers.SerializerMethodField(read_only=True)
    # off_price = serializers.SerializerMethodField(read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.get_image_url()

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()

    # def get_colors(self, obj):
    #     return obj.available_colors()

    # def get_price(self, obj):
    #     return obj.price

    # def get_rate(self, obj):
    #     return obj.get_rate()

    # def get_rate_count(self, obj):
    #     return obj.reviews.count()

    # def get_off_price(self, obj):
    #     return obj.get_off_price()

    class Meta:
        model = models.Product
        fields = "__all__"
        # fields = [
        #     "category",
        #     "name",
        #     "image",
        #     "available",
        #     "brand",
        #     "price",
        #     "material",
        #     "description",
        #     "colors",
        #     "absolute_url",
        # "rate",
        # "rate_count",
        # "off_price",
        # ]


# class ProductVarietySerializer(serializers.ModelSerializer):
#     color = serializers.StringRelatedField(read_only=True)
#     size = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = models.ProductVariety
#         fields = ["product", "color", "size", "sku", "price"]


class ProductDetailSerializer(serializers.ModelSerializer):
    # available_varieties = serializers.SerializerMethodField(read_only=True)
    absolute_url = serializers.SerializerMethodField(read_only=True)

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()

    # def get_available_varieties(self, obj):
    #     return ProductVarietySerializer(
    #         obj.product_varieties.filter(quantity__gt=0), many=True
    #     ).data

    class Meta:
        model = models.Product
        fields = "__all__"
        # fields = [
        #     "category",
        #     "name",
        #     "image",
        #     "available",
        #     "brand",
        #     "material",
        #     "description",
        #     "price",
        #     "material",
        #     "absolute_url",
        #     "available_varieties",
        # ]


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        products = models.Product.objects.filter(
            available=True, category__tree_id=obj.tree_id
        )
        return ProductListSerializer(products, many=True).data

    class Meta:
        model = models.Category
        fields = ["name", "products"]
