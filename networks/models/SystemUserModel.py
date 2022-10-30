from django.db import models

class SystemUser(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    username = models.CharField(max_length=250, blank=False, null=False)
    password = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'SystemUsers'

    def __str__(self):
        return self.name