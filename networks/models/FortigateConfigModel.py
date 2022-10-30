from django.db import models
from .FortigateModel import Fortigate

class FortigateConfig(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    fortigate = models.ForeignKey(Fortigate, on_delete=models.CASCADE, related_name='firewallconfig')

    class Meta:
        db_table = 'FortigateConfigs'

    def __str__(self):
        return self.name