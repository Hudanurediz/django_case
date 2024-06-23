from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='hiringproject_user_set',  # related_name ekleniyor
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='hiringproject_user_set',  # related_name ekleniyor
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.email


class IhaFeatures(models.Model):
    brand = models.CharField(max_length=150, null=False)
    model = models.CharField(max_length=150,null=False)
    weight = models.FloatField()
    category = models.CharField( max_length=150,null=False)
    communication_range= models.CharField(max_length=150, null=False)
    wing_span= models.IntegerField()
    take_off_and_landing=models.CharField(max_length=150)
    payload_capacity=models.CharField(max_length=150)
    thrust_type=models.CharField(max_length=150)
    max_speed=models.BigIntegerField()
    length=models.BigIntegerField()
    operational_altitude=models.BigIntegerField()
    isr=models.CharField(max_length=150)
    hover_time=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)