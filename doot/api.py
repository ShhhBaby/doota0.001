from .models import post
from rest_framework import viewsets, permissions
from .serializers import postSerializer

class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = postSerializer