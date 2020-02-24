from django.shortcuts import render
from .models import PostText

# Create your views here.
def home(request):
    context = {
        'posts': PostText.objects.all()
    }
    return render(request, 'blog/home.html',context)

