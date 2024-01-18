from rest_framework.response import Response 
from rest_framework.decorators import api_view
from booklibrary_app.models import Book
from  .serializers import Bookserializer

@api_view(['GET'])
def getData(request):
    books = Book.objects.all()
    serializer =Bookserializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getoneData(request,id):
    books = Book.objects.get(id =id)
    serializer =Bookserializer(books, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addBook (request):
    serializer = Bookserializer(data =request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateBook (request,id):
    book = Book.objects.get(id=id)
    serializer = Bookserializer(instance=book, data =request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBook (request, id):
    book = Book.objects.get(id =id)
    book.delete()
    return Response()