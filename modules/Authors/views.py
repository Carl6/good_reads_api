from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Author
from .serializers import AuthorSerializer, AuthorBookSerializer
from django.db.models import Q

#antes funciones basadas en vistas, ahora clases basadas en vistas o "Classed base views"
#heredamos estas clases de clase padre APIVIEW HOLA!!!!!
#base views classes a diferencia de en books que aplicamos generic views y podemos escribir lo otro en lugar de esro

class AuthorList(APIView):
    def get(self,request):
        gender = request.query_params.get('gender')
        is_alive = request.query_params.get('is_alive')
        nationality = request.query_params.get('nationality')
        # get_data = request.query_params # todos los query parametros que me pasen en url van a estar dentro de este diccionario
        
        if (gender or is_alive or nationality)is not None:
            authors = Author.objects.filter(Q(gender__icontains=gender) |
                Q(is_alive=bool(is_alive)) |
                Q(nationality__icontains=nationality)
                )
            serializer = AuthorSerializer(authors,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)


            # authors = Author.objects.filter(**get_data) #pasando un diccionario como argumentos... kwargs
            # serializer = AuthorSerializer(authors,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            authors = Author.objects.all() #traeme de la base de datos todos los autores y guardalos en esta variable,.lista de objetos tipo autor...
            serializer = AuthorBookSerializer(authors,many=True) #convertir el array de authors en diccionarios.plus stuff serial en json
            return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = AuthorSerializer(data=request.data) 
        if serializer.is_valid(): #jason pasarlo a tipo autor
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#resource se le llama a una url por ejemplo
#localhost:8000/api/v1/authors/


class AuthorDetail(APIView):
    # def _get_author(self,pk):
    #     try:
    #         autor = Author.objects.get(id=pk)
    #         return autor
    #     except Author.DoesNotExist:
    #         raise  Http404

    def get(self,request,pk):
        autor = get_object_or_404(Author,id=pk)
        serializer = AuthorSerializer(autor)
        return Response(serializer.data,status=status.HTTP_200_OK)


#modificar un autor ya existente
    def put(self,request,pk):
        autor = self._get_author(pk)
        serializer = AuthorSerializer(autor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        autor = self._get_author(pk)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#localhost:8000/api/v1/authors/1/