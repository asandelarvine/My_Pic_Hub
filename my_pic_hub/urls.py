from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path(r'^all/',views.index, name= 'all'),
    re_path(r'^categories/(\d+)',views.categories,name = 'categories'),
    re_path(r'^details/(\d+)',views.details,name = 'details'),
    re_path(r'^search/',views.search, name= 'search')            

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

 
