# Generated by Django 2.1.5 on 2019-04-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
