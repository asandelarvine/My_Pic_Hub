from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image

import pyperclip

# Create your views here.
def index(request):
    all_images = Image.get_images()
    return render(request, 'my-pics/my_pics.html',{"all_images":all_images}) 
    
def home(request):
    return render(request ,'my-pics/home.html')

def categories(request,category):
    category_images = Image.get_images_categories(category)

    def determine_category(category):
        if category == '4':
            return 'Art'
        elif category == '3':
            return 'Sneakers'
        elif category == '2':
            return 'Snacks'
        elif category == '1':
            return 'Musical_Instruments'
        else:
            return 'All'

    message =determine_category(category)

    return render(request,'my-pics/category.html',{"images":category_images,"message":message})

def details(request,photo_id):
    requested_image = Image.objects.get(id= photo_id)
    return render(request,'my-pics/details.html',{"requested_image" :requested_image})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get("image")
        searched_images = Image.search_image_name(search_term)
        message=f"{search_term}"
        return render(request,'my-pics/search.html', {"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my-pics/search.html',{"message":message})

# def image_location(request,location_name):
#     location=Location.get_locations()
#     image= Image.fetch_by_location(location_name)
#     message = f"{location_name}"
#     return render(request, 'details.html',{"message":message,"image": image,"location":location})

# def copyclip(n):
#     domain='https://herokupp.com'
#     path=domain+n
#     full_path=pyperclip.copy(path)
#     return full_path
