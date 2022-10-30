from django.contrib import admin
from .models.FortigateModel import Fortigate
from .models.CiscoSwitchModel import CiscoSwitch
from .models.FortigateConfigModel import FortigateConfig
from .models.CiscoSwitchConfigModel import CiscoSwitchConfig
from .models.SystemUserModel import SystemUser
from .models.ArubaSwitchModel import ArubaSwitch
from .models.ArubaSwitchConfigModel import ArubaSwitchConfig
from .models.HpSwitchModel import HpSwitch
from .models.HpSwitchConfigModel import HpSwitchConfig
from .models.DellSwitchConfigModel import DellSwitchConfig
from .models.DellSwitchModel import DellSwitch
from .models.ExtremeSwitchModel import ExtremeSwitch
from .models.ExtremeSwitchConfigModel import ExtremeSwitchConfig
# Register your models here.

@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'date')
    search_fields = ('name', 'username', 'date')

@admin.register(Fortigate)
class FortigateAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'vendor', 'model', 'address')
    search_fields = ('hostname', 'vendor', 'model', 'address')

@admin.register(FortigateConfig)
class FortigateConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('hostname', 'date')

@admin.register(CiscoSwitch)
class CiscoSwitchAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'vendor', 'model', 'address')
    search_fields = ('hostname', 'vendor', 'model', 'address')

@admin.register(CiscoSwitchConfig)
class CiscoSwitchConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('hostname', 'date')

@admin.register(ArubaSwitch)
class ArubaSwitchAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'vendor', 'model', 'address')
    search_fields = ('hostname', 'vendor', 'model', 'address')

@admin.register(ArubaSwitchConfig)
class ArubaSwitchConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('hostname', 'date')

@admin.register(HpSwitch)
class HpSwitchAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'vendor', 'model', 'address')
    search_fields = ('hostname', 'vendor', 'model', 'address')

@admin.register(HpSwitchConfig)
class HpSwitchConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('hostname', 'date')

@admin.register(DellSwitch)
class DellSwitchAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'vendor', 'model', 'address')
    search_fields = ('hostname', 'vendor', 'model', 'address')

@admin.register(DellSwitchConfig)
class DellSwitchConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('hostname', 'date')

@admin.register(ExtremeSwitch)
class ExtremeSwitchAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'vendor', 'model', 'address')
    search_fields = ('hostname', 'vendor', 'model', 'address')

@admin.register(ExtremeSwitchConfig)
class ExtremeSwitchConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('hostname', 'date')