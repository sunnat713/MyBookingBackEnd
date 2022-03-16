from django.contrib.auth.models import AbstractUser
from django.db import models
from config.helpers import UploadTo
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to=UploadTo("client/avatar"), blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    # def save(self, **kwargs):
    #     if self.
    #     self.set_password()
    #     return super().save(**kwargs)

@receiver(pre_save, sender=User)
def user_signal(sender, instance, created, **kwargs):
    if created or instance.pk:
        user = User.objects.get(pk=instance.pk)
        
        instance.set_password(instance.password)
        instance.save()
        print(instance.password)