from django.contrib.auth.models import AbstractUser
from django.db import models
from config.helpers import UploadTo
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password
from rest_framework.validators import ValidationError

class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to=UploadTo("client/avatar"), blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

 
@receiver(pre_save, sender=User)
def user_signal(sender, instance, **kwargs):
    if instance.pk:
        pswd_checked = False
        old_password = User.objects.get(pk=instance.pk).password
        print(pswd_checked)
        # if instance.new:
        #     pswd_checked = check_password(instance.new, old_password)
        # elif instance.password:
        #     pswd_checked = check_password(instance.password, old_password)
            
        # if not pswd_checked:
        #     instance.set_password(instance.password)
        # else:
        #     raise ValidationError(_("Joriy parolingizni qayta kiritdingiz yangi parol kiriting!"))
    else:
        instance.set_password(instance.password)