from apscheduler.schedulers.background import BackgroundScheduler
from .routers.DellHelper import dell_switch_all_task_sync
from .routers.ArubaHelper import aruba_switch_all_task_sync
from .routers.CiscoHelpers import cisco_switch_all_task_sync
from .routers.ExtremeHelper import extreme_switch_all_task_sync
from .routers.HpHelper import hp_switch_all_task_sync
from .firewalls.FortigateHelper import fortigate_all_task_sync
import os

def schedulebackup():
    fortigate_all_task_sync()
    cisco_switch_all_task_sync()
    aruba_switch_all_task_sync()
    dell_switch_all_task_sync()
    extreme_switch_all_task_sync()
    hp_switch_all_task_sync()

def sybg():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedulebackup, 'interval', hours=12)
    scheduler.start()