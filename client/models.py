from django.contrib.auth.models import AbstractUser
from django.db import models
from config.helpers import UploadTo
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password
from rest_framework.validators import ValidationError
from django.templatetags.static import static

class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to=UploadTo("client/avatar"), blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    status = models.CharField(max_length=1, choices=( ("1",_("owner")), ("2", _("user")) ), default="2", null=True)
    
    @property
    def avatar(self):
        if self.photo:
            return self.photo.url
        
        return static("img/no_photo.png")


@receiver(pre_save, sender=User)
def user_signal(sender, instance, **kwargs):
    if instance.pk:
        pswd_checked = False
        new_pswd = None
        try:
            new_pswd = getattr(instance, 'new')
        except:
            new_pswd = getattr(instance, "password")
        else:
            pass
        if not new_pswd.startswith("pbkdf2_sha256"):
            instance.set_password(new_pswd)

    else:
        instance.set_password(instance.password)