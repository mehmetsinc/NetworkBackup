from django.db import models
from .SystemUserModel import SystemUser

class CiscoSwitch(models.Model):
    hostname = models.CharField(max_length=150, blank=False, null=False)
    vendor = models.CharField(max_length=150, blank=True, null=True)
    model = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, blank=False, null=False)
    serial = models.CharField(max_length=150, blank=True, null=True)
    version = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    systemuser = models.ForeignKey(SystemUser, on_delete=models.CASCADE, related_name='ciscoswitch')

    class Meta:
        db_table = 'CiscoSwitchs'

    def __str__(self):
        return self.hostname


