from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Review
from .serializers import ReviewSerializer

def index(request):
	return render(request, "app/index.html")

class ReviewViewSet(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer