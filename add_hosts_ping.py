#!/usr/bin/env python

from uptime_kuma_api import UptimeKumaApi, MonitorType

with UptimeKumaApi('http://uptimekuma01:3001') as api:
    api.login('username', 'password')
    api.add_monitor(
        type=MonitorType.PING,
        name="host01",
        hostname="host01"
    )
    api.add_monitor(
        type=MonitorType.PING,
        name="host02",
        hostname="host02"
    )
    api.add_monitor(
        type=MonitorType.PING,
        name="host03",
        hostname="host03"
    )
    api.add_monitor(
        type=MonitorType.PING,
        name="host04",
        hostname="host04"
    )
    api.add_monitor(
        type=MonitorType.PING,
        name="host05",
        hostname="host05"
    )
