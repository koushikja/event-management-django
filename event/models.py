from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User

class UserDetail(models.Model):
    userinfo=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.IntegerField(choices=((1,("user")),(2,("lessor")),(3,("service"))))
    user_address = models.TextField(max_length=140,null=True)
    user_phone = models.CharField(max_length=13,null=True)

    def __str__(self):
        return self.userinfo.username


class Place(models.Model):
    place_name=models.CharField(max_length=30)
    place_address=models.TextField()
    place_owner= models.ForeignKey(User,on_delete=models.CASCADE)
    place_description=models.TextField()
    place_price=models.IntegerField(default=0)
    place_image = models.ImageField(null=True, blank=True, upload_to="projects-images/")


    def __str__(self):
        return self.place_name

class Service(models.Model):
    service_name=models.CharField(max_length=20)
    service_description=models.TextField()
    service_price=models.IntegerField(default=0)
    service_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    service_image = models.ImageField(null=True, blank=True, upload_to="projects-images/")

    def __str__(self):
        return self.service_name


class MicroBlog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=20)
    blog_content=models.TextField()

    def __str__(self):
        return self.user.username


# Create your models here.
