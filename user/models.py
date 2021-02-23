from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20,verbose_name='昵称')
    Avatar = models.ImageField(upload_to='avatar/%Y%m%d/',blank=True)

    def __str__(self):
        return '<Profile: %s for %s>' %(self.nickname,self.user.username)

#动态绑定
def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        if profile.nickname!='':
            return profile.nickname
        else:
            return self.username
    else:
        return self.username

def has_nickname(self):
    return Profile.objects.filter(user=self).exists()

def get_avatar(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        try:
            return profile.Avatar.url
        except:
            return "/media/default/unlogin.png"

    else:
        return "/media/default/unlogin.png"

User.get_nickname = get_nickname
User.get_avatar = get_avatar