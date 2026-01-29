from django.db import models

from django.contrib.auth.models import User

class Thought(models.Model):

    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True, default='Default.png', upload_to='media/')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


