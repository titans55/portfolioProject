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

    def __str__(self):
        return self.time

class Experience(models.Model):
    header = models.CharField(max_length=200, null=False)
    subheader = models.CharField(max_length=200, null=True, blank=True)
    description =  models.CharField(max_length=500, null=True, blank=True)
    startedAt = models.CharField(max_length=100, null=False)
    endedAt = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.header

class PlAndTech(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Workflow(models.Model):
    description = models.CharField(max_length=500, null=False)
    def __str__(self):
        return self.description

class Interest(models.Model):
    description = models.CharField(max_length=500, null=False)
    def __str__(self):
        return self.description

class Education(models.Model):
    header = models.CharField(max_length=200, null=False)
    subheader = models.CharField(max_length=200, null=True, blank=True)
    description =  models.CharField(max_length=500, null=True, blank=True)
    startedAt = models.CharField(max_length=100, null=False)
    endedAt = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.header
        
class About(models.Model): 
    about = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.about