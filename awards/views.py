from django.shortcuts import render,redirect
from django.http.response import Http404
# from .serializers import ProfileSerializer, ProjectSerializer
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import generics

from django.http  import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserUpdateForm, ProfileUpdateForm, ProjectUploadForm, UserRegisterForm, RateForm
from awards.models import Project,User,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'home.html', {"projects":projects, "users": users})

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})


class ListProjectView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer