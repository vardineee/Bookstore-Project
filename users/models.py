from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    image = models.ImageField(upload_to=None, null=True, blank=True,
                              default='media/None/default.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    gender = models.CharField(max_length=30, choices=CHOICES, blank=True, null=True)
    username = models.CharField(blank=True, null= True, max_length=100)
    owner = models.BooleanField(default=False)
