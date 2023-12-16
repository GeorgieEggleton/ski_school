from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Lesson

@receiver(post_save, sender=Lesson)
def update_on_save(sender, instance, created, **kwargs):
    instance.remaining_capacity = instance.type.max_capacity - instance.students.count()
    print(f"I'm here")