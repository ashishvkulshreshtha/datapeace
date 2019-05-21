from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, help_text='Please provide valid Email only.')
    web = models.URLField(blank=True, null=True, help_text='Please provide valid URL only.')
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name
