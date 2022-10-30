from django.db import models
from .ExtremeSwitchModel import ExtremeSwitch

class ExtremeSwitchConfig(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    extremeswitch = models.ForeignKey(ExtremeSwitch, on_delete=models.CASCADE, related_name='extremeswitchconfig')

    class Meta:
        db_table = 'ExtremeSwitchConfigs'

    def __str__(self):
        return self.name