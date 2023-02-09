from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

# ********************************************************
#   '''классы-дженерики в DRF'''
# from rest_framework import generics

# from .models import Cat
# from .serializers import CatSerializer


# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

# ********************************************************
#   '''Низкоуровневые view-классы в DRF'''
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from .models import Cat
# from .serializers import CatSerializer


# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)
    

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()  
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class APICatDetail(APIView):
#     def get(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         serializer = CatSerializer(cat)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         serializer = CatSerializer(cat, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
#     def patch(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
       
#     def delete(self, request, pk):
#         cat = Cat.objects.get(pk=pk)
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ********************************************************
#   '''функции в DRF'''
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def api_cats_detail(request, pk):
#     cat = Cat.objects.get(pk=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = CatSerializer(cat)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         # Создаём объект сериализатора 
#         # и передаём в него данные из POST-запроса
#         serializer = CatSerializer(data=request.data)        
#         if serializer.is_valid():
#             serializer.save()
#             # Возвращаем JSON со всеми данными нового объекта
#             # и статус-код 201
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Если данные не прошли валидацию — 
#         # возвращаем информацию об ошибках и соответствующий статус-код:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # В случае GET-запроса возвращаем список всех котиков
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data) 