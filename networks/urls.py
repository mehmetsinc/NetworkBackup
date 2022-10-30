from django.urls import path
from networks.views.HomeView import network_home
from networks.views.SystemUserView import system_user_view, system_user_create, system_user_update_view, system_user_delete_view
from networks.views.FortigateView import *
from networks.views.CiscoSwitchView import *
from networks.views.ArubaSwitchView import *
from networks.views.HpSwitchView import *
from networks.views.DellSwitchView import *
from networks.views.ExtremeSwitchView import *
urlpatterns = [
    path('', network_home, name='home'),

    path('systemusers', system_user_view, name='system_user_view'),
    path('systemusercreate', system_user_create, name='system_user_create'),
    path('systemuserupdate/<int:id>', system_user_update_view, name='system_user_update_view'),
    path('systemuserdelete/<int:id>', system_user_delete_view, name='system_user_delete_view'),

    path('fortigates', fortigate_view, name='fortigate_view'),
    path('fortigateallsync', fortigate_all_sync_view, name='fortigate_all_sync_view'),
    path('fortigatecreate', fortigate_create_view, name='fortigate_create_view'),
    path('fortigateupdate/<int:id>', fortigate_update_view, name='fortigate_update_view'),
    path('fortigatedelete/<int:id>', fortigate_delete_view, name='fortigate_delete_view'),
    path('fortigatebackup/<int:id>', fortigate_backup_sync_view, name='fortigate_backup_sync_view'),
    path('fortigatesystem/<int:id>', fortigate_system_sync_view, name='fortigate_system_sync_view'),
    path('fortigateconfiglist/<int:id>', fortigate_config_view, name='fortigate_config_view'),
    path('fortigateconfigdetail/<int:id>', fortigate_config_detail_view, name='fortigate_config_detail_view'),
    path('fortigateconfigdelete/<int:id>', fortigate_config_delete_view, name='fortigate_config_delete_view'),

    path('cisco_switcies', cisco_switch_view, name='cisco_switch_view'),
    path('cisco_switchallsync', cisco_switch_all_sync_view, name='cisco_switch_all_sync_view'),
    path('cisco_switch_create', cisco_switch_create_view, name='cisco_switch_create_view'),
    path('cisco_switch_update/<int:id>', cisco_switch_update_view, name='cisco_switch_update_view'),
    path('cisco_switch_delete/<int:id>', cisco_switch_delete_view, name='cisco_switch_delete_view'),
    path('cisco_switch_backup/<int:id>', cisco_switch_backup_sync_view, name='cisco_switch_backup_sync_view'),
    path('cisco_switch_system/<int:id>', cisco_switch_system_sync_view, name='cisco_switch_system_sync_view'),
    path('ciscoswitchconfiglist/<int:id>', cisco_switch_config_view, name='cisco_switch_config_view'),
    path('ciscoswitchconfigdetail/<int:id>', cisco_switch_config_detail_view, name='cisco_switch_config_detail_view'),
    path('ciscoswitchconfigdelete/<int:id>', cisco_switch_config_delete_view, name='cisco_switch_config_delete_view'),

    path('aruba_switcies', aruba_switch_view, name='aruba_switch_view'),
    path('aruba_switchallsync', aruba_switch_all_sync_view, name='aruba_switch_all_sync_view'),
    path('aruba_switch_create', aruba_switch_create_view, name='aruba_switch_create_view'),
    path('aruba_switch_update/<int:id>', aruba_switch_update_view, name='aruba_switch_update_view'),
    path('aruba_switch_delete/<int:id>', aruba_switch_delete_view, name='aruba_switch_delete_view'),
    path('aruba_switch_backup/<int:id>', aruba_switch_backup_sync_view, name='aruba_switch_backup_sync_view'),
    path('aruba_switch_system/<int:id>', aruba_switch_system_sync_view, name='aruba_switch_system_sync_view'),
    path('arubaswitchconfiglist/<int:id>', aruba_switch_config_view, name='aruba_switch_config_view'),
    path('arubaswitchconfigdetail/<int:id>', aruba_switch_config_detail_view, name='aruba_switch_config_detail_view'),
    path('arubaswitchconfigdelete/<int:id>', aruba_switch_config_delete_view, name='aruba_switch_config_delete_view'),

    path('hp_switcies', hp_switch_view, name='hp_switch_view'),
    path('hp_switchallsync', hp_switch_all_sync_view, name='hp_switch_all_sync_view'),
    path('hp_switch_create', hp_switch_create_view, name='hp_switch_create_view'),
    path('hp_switch_update/<int:id>', hp_switch_update_view, name='hp_switch_update_view'),
    path('hp_switch_delete/<int:id>', hp_switch_delete_view, name='hp_switch_delete_view'),
    path('hp_switch_backup/<int:id>', hp_switch_backup_sync_view, name='hp_switch_backup_sync_view'),
    path('hp_switch_system/<int:id>', hp_switch_system_sync_view, name='hp_switch_system_sync_view'),
    path('hpswitchconfiglist/<int:id>', hp_switch_config_view, name='hp_switch_config_view'),
    path('hpswitchconfigdetail/<int:id>', hp_switch_config_detail_view, name='hp_switch_config_detail_view'),
    path('hpswitchconfigdelete/<int:id>', hp_switch_config_delete_view, name='hp_switch_config_delete_view'),

    path('dell_switcies', dell_switch_view, name='dell_switch_view'),
    path('dell_switchallsync', dell_switch_all_sync_view, name='dell_switch_all_sync_view'),
    path('dell_switch_create', dell_switch_create_view, name='dell_switch_create_view'),
    path('dell_switch_update/<int:id>', dell_switch_update_view, name='dell_switch_update_view'),
    path('dell_switch_delete/<int:id>', dell_switch_delete_view, name='dell_switch_delete_view'),
    path('dell_switch_backup/<int:id>', dell_switch_backup_sync_view, name='dell_switch_backup_sync_view'),
    path('dell_switch_system/<int:id>', dell_switch_system_sync_view, name='dell_switch_system_sync_view'),
    path('dellswitchconfiglist/<int:id>', dell_switch_config_view, name='dell_switch_config_view'),
    path('dellswitchconfigdetail/<int:id>', dell_switch_config_detail_view, name='dell_switch_config_detail_view'),
    path('dellswitchconfigdelete/<int:id>', dell_switch_config_delete_view, name='dell_switch_config_delete_view'),

    path('extreme_switcies', extreme_switch_view, name='extreme_switch_view'),
    path('extreme_switchallsync', extreme_switch_all_sync_view, name='extreme_switch_all_sync_view'),
    path('extreme_switch_create', extreme_switch_create_view, name='extreme_switch_create_view'),
    path('extreme_switch_update/<int:id>', extreme_switch_update_view, name='extreme_switch_update_view'),
    path('extreme_switch_delete/<int:id>', extreme_switch_delete_view, name='extreme_switch_delete_view'),
    path('extreme_switch_backup/<int:id>', extreme_switch_backup_sync_view, name='extreme_switch_backup_sync_view'),
    path('extreme_switch_system/<int:id>', extreme_switch_system_sync_view, name='extreme_switch_system_sync_view'),
    path('extremeswitchconfiglist/<int:id>', extreme_switch_config_view, name='extreme_switch_config_view'),
    path('extremeswitchconfigdetail/<int:id>', extreme_switch_config_detail_view, name='extreme_switch_config_detail_view'),
    path('extremeswitchconfigdelete/<int:id>', extreme_switch_config_delete_view, name='extreme_switch_config_delete_view'),
]
