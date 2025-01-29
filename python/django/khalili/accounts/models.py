from django.db import models
from django.db.models.signals import post_save,post_delete,pre_save,pre_delete,m2m_changed
from django.core.signals import request_started,request_finished
from django.contrib.auth.models import User
from phone_field import PhoneField
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = PhoneField(null=True,blank=True)
    address = models.CharField(max_length=122,null=True,blank=True)
    def __str__(self):
        return self.user.username
def save_profile_user(sender,**kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])  # تغییر User به user
        profile_user.save()
post_save.connect(save_profile_user,sender=User)

#چرا از user ستفاده کرد نه User


