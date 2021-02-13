from django.shortcuts import render

# Create your views here.

def love_images(request):
    return render(request, 'auto_images/index.html')