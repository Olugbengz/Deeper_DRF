from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

#  Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):

    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Error":"Enter the rigth data"}, status=400)

    
    # print(request.GET)
    # print(request.POST)
    # body = request.body
    # data = {}
    # try: 
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data.keys)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type












