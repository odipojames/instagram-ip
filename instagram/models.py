from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to ='images/')
    bio = models.TextField()

    def __str__(self):
        return self.name.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls,identity):
        profile = Profile.objects.filter(name__username__icontains = identity)
        return profile

    @classmethod
    def delete_profile(cls,id):
        prof= Profile.objects.filter(id = id)
        prof.delete()

    @classmethod
    def search_profile(cls,jina):
        profile = Profile.objects.filter(name__username__icontains=jina)
        return profile

class Like(models.Model):
    likes = models.IntegerField(null = True)

    def __int__(self):
        return self.likes

    def save_comment(self):
        self.save()

class Comment(models.Model):
    comments =models.CharField(max_length= 80,blank= True)
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('app.Image', on_delete=models.CASCADE, related_name='opinions')

    def __str__(self):
        return self.comments

    def save_comment(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 50)
    profile = models.ForeignKey(Profile)
    likes = models.ForeignKey(Like)
    comments = models.ForeignKey(Comment,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def get_image(cls,id):
        image = Image.objects.filter(id = id)
        return image

    @classmethod
    def get_post(cls,jina):
        images = Image.objects.filter(profile__name__username__icontains = jina)
        return images

    @classmethod
    def delete_image(cls,id):
        image = Image.objects.filter(id = id)
        image.delete()

    @classmethod
    def update_caption(cls,id,cap):
        image = Image.objects.filter(id=id)
        image.update(image_caption = cap)
        return image
