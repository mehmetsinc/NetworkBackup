from django.db import models
from .CiscoSwitchModel import CiscoSwitch

class CiscoSwitchConfig(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    ciscoswitch = models.ForeignKey(CiscoSwitch, on_delete=models.CASCADE, related_name='ciscoswitchconfig')

    class Meta:
        db_table = 'CiscoSwitchConfigs'

    def __str__(self):
        return self.name