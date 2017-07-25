from .models import Book
from rest_framework import generics,filters
from .serializers import *
from rest_framework.permissions import IsAdminUser
from .permissions import CarlaPermission
import django_filters.rest_framework


# Create your views here.
# esto se llama generic views a diferencia de bases views que usamos en el otro
#vistas genericas son como templates en codigo

class BookList(generics.ListCreateAPIView):
    # permission_classes = (IsAdminUser,)
    # permission_classes = (CarlaPermission,)
    serializer_class = BookSerializer 
    queryset = Book.objects.all()
    filter_backends =(filters.SearchFilter,
    django_filters.rest_framework.DjangoFilterBackend)
    filter_fields = ('name','ISBN','author','lit_genre')
    search_fields = ('name','ISBN','summary')

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookAuthorList(generics.ListAPIView):
    serializer_class = BookAuthorSerializer
    queryset = Book.objects.all()
