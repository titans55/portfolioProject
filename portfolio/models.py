from django.db import models
#*
# The Model to represent the hit table in the DB
# *#
class Hit(models.Model):
    page_name = models.CharField(max_length=300, null=True)
    endpoint = models.CharField(max_length=300, null=True)
    country = models.CharField(max_length=300, null=True)
    device_ip = models.GenericIPAddressField()
    browser = models.CharField(max_length=300)
    os = models.CharField(max_length=300)
    referer = models.URLField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=300, null=True)
    mobile = models.BooleanField(null=True)
    tablet = models.BooleanField(null=True)
    touch = models.BooleanField(null=True)
    pc = models.BooleanField(null=True)
    bot = models.BooleanField(null=True)