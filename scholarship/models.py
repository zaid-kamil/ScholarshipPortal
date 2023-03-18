import django_filters
from django.db import models
from django.utils import timezone
from image_optimizer.fields import OptimizedImageField

from .utils import COUNTRIES


class Scholarship(models.Model):
    name = models.CharField(max_length=255, help_text='Name of the scholarship')
    country = models.CharField(max_length=255, choices=COUNTRIES.items(), help_text='Country of the scholarship')
    amount = models.CharField(max_length=255, help_text='Amount of the scholarship', default='$100')
    description = models.TextField(help_text='Description of the scholarship')
    eligibility = models.TextField(help_text='Eligibility criteria for the scholarship')
    acceptance_start_date = models.DateField(help_text='Start date to apply for the scholarship', default=timezone.now)
    winner_announcement_date = models.DateField(help_text='Date when the winner will be announced',
                                                default=timezone.now() + timezone.timedelta(days=15))
    quantity = models.IntegerField(help_text='Number of scholarships available', default=1)
    last_date = models.DateField(help_text='Last date to apply for the scholarship',
                                 default=timezone.now() + timezone.timedelta(days=30))
    link = models.URLField(help_text='Link to the scholarship page')
    organization = models.CharField(max_length=255, help_text='Organization providing the scholarship',
                                    default='Organization Name')
    image = OptimizedImageField(upload_to='scholarship_pics',
                                blank=True,
                                null=True,
                                optimized_image_resize_method='cover',
                                optimized_image_output_size=(512, 512))

    def __str__(self):
        return self.name

    def is_active(self):
        return self.last_date > timezone.now()

    def amt_indian(self):
        if '$' in self.amount:
            return int(self.amount.split('$')[1]) * 80
        elif '€' in self.amount:
            return int(self.amount.split('€')[1]) * 100
        elif '£' in self.amount:
            return int(self.amount.split('£')[1]) * 120
        else:
            return self.amount

    class Meta:
        verbose_name_plural = 'Scholarships'


class ScholarshipFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.ChoiceFilter(choices=list(COUNTRIES.items()))
    organization = django_filters.CharFilter(lookup_expr='icontains')
    quantity = django_filters.NumberFilter(field_name='quantity')
    start_date = django_filters.DateRangeFilter(field_name='acceptance_start_date')
    o = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
        ))

    class Meta:
        model = Scholarship
        fields = ['name', 'country', 'organization', 'start_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super(ScholarshipFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label = 'Scholarship Name'
        self.filters['country'].label = 'Country'
        self.filters['organization'].label = 'Organization'
        self.filters['quantity'].label = 'Total Scholarships'
        self.filters['start_date'].label = 'Start Date'
