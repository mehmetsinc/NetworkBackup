from django.db import models
from .DellSwitchModel import DellSwitch

class DellSwitchConfig(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    dellswitch = models.ForeignKey(DellSwitch, on_delete=models.CASCADE, related_name='dellswitchconfig')

    class Meta:
        db_table = 'DellSwitchConfigs'

    def __str__(self):
        return self.name