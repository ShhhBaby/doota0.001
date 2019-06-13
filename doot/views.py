from django.shortcuts import render, redirect, get_object_or_404
from .forms import postForm
from .models import post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import postSerializer
# Create your views here.

def post_view(request):
    
    queryset = post.objects.all()
    queryset = queryset.reverse()
    context = {
        'post_list' : queryset,
    }
    
    
    
    return render(request, 'home.html', context)


def user_view(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user
           
            post.save()
            return redirect('home')
    else:
        form = postForm()
    return render(request, 'user.html', {'form': form})

#class postListJSON(APIView):

 #   def get(self, request):
  #      PostList = post.objects.all()
   #     serializer = postSerializer(PostList, many=True)
    #    return Response(serializer.data)
    
  #  def post(self):
    #    pass