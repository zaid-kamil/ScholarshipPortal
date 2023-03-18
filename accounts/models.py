import re

from django.contrib.auth.models import User
from django.db import models
from image_optimizer.fields import OptimizedImageField


# Create your profile model and link it with the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = OptimizedImageField(upload_to='profile_pics', blank=True, null=True, optimized_image_resize_method='thumbnail', optimized_image_output_size=(128, 128))
    gender = models.CharField(choices=(('M', 'Male'), ('F', 'Female')), max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # validate the phone number
        if self.phone:
            self.phone = self.validate_phone()
        super().save(*args, **kwargs)

    # validate indian phone number using regex
    def validate_phone(self):
        if self.phone:
            if not re.match(r'^[6-9]\d{9}$', self.phone):
                raise ValueError('Invalid Indian phone number')
        return self.phone
