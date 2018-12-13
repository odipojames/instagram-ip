from django.test import TestCase
from .models import *

# Create your tests here.

class ImageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='j')
        self.profile = Profile.objects.create(name = self.user,bio = 'bb')
        self.likes = Like.objects.create(likes = 1)
        self.image = Image.objects.create(image_name = 'kk',
                                          id = 1,
                                          image_caption ='ww',
                                          likes = self.likes,
                                          profile = self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_delete(self):
        self.image.save()
        self.image.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_get_image(self):
        self.image.save()
        image = Image.get_image(1)
        self.assertTrue(len(image) == 1)

    def test_get_post(self):
        self.image.save()
        image = Image.get_post('j')
        self.assertTrue(len(image) == 1)

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='j')
        self.profile = Profile.objects.create(name = self.user,bio = 'bb')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile('j')
        self.assertTrue(len(profile)== 1)

    def test_delete(self):
        self.profile.save()
        self.profile.delete()
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_search_profile(self):
        self.profile.save()
        profile = Profile.search_profile('j')
        self.assertTrue(len(profile)== 1)

class likesTest(TestCase):

    def setUp(self):
        self.likes = Like.objects.create(likes=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.likes,Like))
