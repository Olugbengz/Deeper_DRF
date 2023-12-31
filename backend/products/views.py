from rest_framework import authentication, generics, permissions
from api.authentication import TokenAuthentication
from api.mixins import (
    IsStaffEditorPermission, 
    UserQuerySetMixin
    )
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(
    UserQuerySetMixin,
    IsStaffEditorPermission,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    def perform_create(self, serializer):
        print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.object.none()

        return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    IsStaffEditorPermission,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = pk  


product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    IsStaffEditorPermission,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    IsStaffEditorPermission,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  

 
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDestroyAPIView.as_view()












 

# class ProductMixinView(
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     generics.GenericAPIView
#     ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args, **kwargs)

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = pk  


# product_list_view = ProductListAPIView.as_view()
