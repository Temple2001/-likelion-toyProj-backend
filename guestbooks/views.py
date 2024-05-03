from django.shortcuts import render
from django.shortcuts import get_object_or_404
from guestbooks.models import *

from .serializers import GuestbookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class GuestbookList(APIView):
    def get(self, request, format=None):
        guestbooks = Guestbook.objects.all()
        serializer = GuestbookSerializer(guestbooks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuestbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuestbookDetail(APIView):
    def delete(self, request, id):
        guestbook = get_object_or_404(Guestbook, id=id)
        password = request.data.get('password')
        print(password)
        if guestbook.password == password:
            guestbook.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)