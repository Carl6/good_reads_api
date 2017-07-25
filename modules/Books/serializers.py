from rest_framework import serializers
from .models import Book
#from modules.Authors.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # exclude = ('rating',)
        fields = ("__all__")

class BookAuthorSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only = True)
    
    class Meta:
        model = Book
        fields = ("__all__")
