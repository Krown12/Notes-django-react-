from django.shortcuts import render
from .serializers import *
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import generics


class UserView(generics.CreateAPIView):
    model = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[AllowAny,]


class NotesListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes =[IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)
    
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)