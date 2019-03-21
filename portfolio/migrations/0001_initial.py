# Generated by Django 2.1.5 on 2019-03-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=300, null=True)),
                ('endpoint', models.CharField(max_length=300, null=True)),
                ('device_ip', models.GenericIPAddressField()),
                ('browser', models.CharField(max_length=300)),
                ('os', models.CharField(max_length=300)),
                ('referer', models.URLField(null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('device', models.CharField(max_length=300, null=True)),
                ('mobile', models.BooleanField(null=True)),
                ('tablet', models.BooleanField(null=True)),
                ('touch', models.BooleanField(null=True)),
                ('pc', models.BooleanField(null=True)),
                ('bot', models.BooleanField(null=True)),
            ],
        ),
    ]
