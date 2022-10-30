from django.db import models
from .HpSwitchModel import HpSwitch

class HpSwitchConfig(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    hpswitch = models.ForeignKey(HpSwitch, on_delete=models.CASCADE, related_name='hpswitchconfig')

    class Meta:
        db_table = 'HpSwitchConfigs'

    def __str__(self):
        return self.name