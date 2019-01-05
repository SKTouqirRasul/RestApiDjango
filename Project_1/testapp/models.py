from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
'''
class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model,using=self._db)
'''

def upload_status_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)


class Status(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True,blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #objects = StatusManager()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status posts '
