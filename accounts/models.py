import re

from django.contrib.auth.models import User
from django.db import models
from image_optimizer.fields import OptimizedImageField


class EducationChoices(models.TextChoices):
    HIGHSCHOOL = (1, 'High School')
    INTERMEDIATE = (2, 'Intermediate')
    BACHELOR_TECH = (3, 'B.Tech')
    BACHELOR_ARTS = (4, 'B.A')
    BACHELOR_SCIENCE = (5, 'B.Sc')
    BACHELOR_COMMERCE = (6, 'B.Com')
    BACHELOR_LAW = (7, 'B.L')
    BACHELOR_ENGINEERING = (8, 'B.E')
    BACHELOR_MEDICAL = (9, 'B.M')
    BACHELOR_PHARMACY = (10, 'B.Pharm')
    MASTER_TECH = (11, 'M.Tech')
    MASTER_ARTS = (12, 'M.A')
    MASTER_SCIENCE = (13, 'M.Sc')
    MASTER_COMMERCE = (14, 'M.Com')
    MASTER_LAW = (15, 'M.L')
    MASTER_ENGINEERING = (16, 'M.E')
    MASTER_MEDICAL = (17, 'M.M')
    MASTER_PHARMACY = (18, 'M.Pharm')
    DOCTORATE = (19, 'Ph.D')


# Create your profile model and link it with the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = OptimizedImageField(upload_to='profile_pics', blank=True, null=True,
                                optimized_image_resize_method='thumbnail', optimized_image_output_size=(128, 128))
    gender = models.CharField(choices=(('M', 'Male'), ('F', 'Female')), max_length=1, default='F')
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(choices=EducationChoices.choices, default=EducationChoices.BACHELOR_TECH, max_length=2)

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
