from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class ThreadListView(generics.ListCreateAPIView):
    pass
