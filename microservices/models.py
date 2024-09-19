from django.db import models


class Service(models.Model):

    name = models.CharField(max_length=32)
    url = models.CharField(max_length=256, null=True, blank=True,help_text='Not required if running locally')
    local = models.BooleanField(default=True,help_text='Check if running locally')
    active = models.BooleanField(default=True)
    manage = models.CharField(max_length=256, unique=True,help_text="Full path to the directory that the project's manage.py file is in")
    setting= models.CharField(max_length=256, unique=True,help_text="Full path to the directory that the project's settings.py file is in")
    virtual_env = models.CharField(max_length=256, null=True, blank=True,help_text="Ful path to the directory that your virtual environment's bin directory is in")


    def __str__(self):
        return self.name


