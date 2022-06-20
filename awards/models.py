from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    profile_photo = CloudinaryField('profile_photo', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Project(models.Model):
    title = models.CharField(max_length = 60)
    project_image = CloudinaryField('project_image', null=True)
    description = models.TextField()
    link = models.CharField(max_length = 200, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    prof_ref = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', null=True)

class Meta:
    
        ordering = ['pub_date']

def __str__(self):
        return self.title

def no_of_ratings(self):
        ratings = Rating.objects.filter(project=self)
        return len(ratings)


def average_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(project=self)
        for rating in ratings:
            sum += ((rating.rate_design + rating.rate_usability + rating.rate_content)/3)
        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

@classmethod
def search_project(cls, search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project