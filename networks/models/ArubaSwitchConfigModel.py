from django.db import models
from .ArubaSwitchModel import ArubaSwitch

class ArubaSwitchConfig(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    arubaswitch = models.ForeignKey(ArubaSwitch, on_delete=models.CASCADE, related_name='arubaswitchconfig')

    class Meta:
        db_table = 'ArubaSwitchConfigs'

    def __str__(self):
        return self.name