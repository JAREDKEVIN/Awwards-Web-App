from django.urls import re_path,path
from . import views
from django.contrib.auth import views as auth_views
from .views import ListProfileView, ListProjectView

urlpatterns = [
path('',views.home,name = 'home'),

]
