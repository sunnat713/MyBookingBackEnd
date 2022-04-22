from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

@receiver(post_save)
def update_document(sender, **kwargs):
    print("SIGNAL WORK")
    pass
