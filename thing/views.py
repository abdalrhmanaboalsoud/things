from django.shortcuts import render
from .models import Thing
from .serialaizer import ThingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOnly
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class ThingList(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsAuthenticated]  # Corrected typo here

    def perform_create(self, serializer):
        # Ensure the owner is set to the current user
        serializer.save(owner=self.request.user)


class ThingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsOwnerOnly]  # Corrected typo here
