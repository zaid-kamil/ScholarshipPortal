# Generated by Django 4.1.7 on 2023-04-13 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0015_scholarship_education_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='education_level',
            field=models.CharField(choices=[('1', 'High School'), ('2', 'Intermediate'), ('3', 'B.Tech'), ('4', 'B.A'), ('5', 'B.Sc'), ('6', 'B.Com'), ('7', 'B.L'), ('8', 'B.E'), ('9', 'B.M'), ('10', 'B.Pharm'), ('11', 'M.Tech'), ('12', 'M.A'), ('13', 'M.Sc'), ('14', 'M.Com'), ('15', 'M.L'), ('16', 'M.E'), ('17', 'M.M'), ('18', 'M.Pharm'), ('19', 'Ph.D')], default='3', max_length=2),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 5, 15, 52, 740721, tzinfo=datetime.timezone.utc), help_text='Last date to apply for the scholarship'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='winner_announcement_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 28, 5, 15, 52, 740721, tzinfo=datetime.timezone.utc), help_text='Date when the winner will be announced'),
        ),
    ]
