from django.db import models
from django.contrib.auth.models import User
from reito import settings
from cloudinary.models import CloudinaryField


User._meta.get_field('email')._unique = True
User._meta.get_field('email').null = False
User._meta.get_field('email').blank = False

# Model representing a user of the system.
class Usuario(User):
    telefono = models.BigIntegerField(unique=True, blank=False, null=False)
    foto = CloudinaryField('image', default=None, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()
