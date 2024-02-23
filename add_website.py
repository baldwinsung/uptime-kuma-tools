#!/usr/bin/env python

from uptime_kuma_api import UptimeKumaApi, MonitorType

with UptimeKumaApi('http://uptimekuma01:3001') as api:
    api.login('username', 'password')
    api.add_monitor(
        type=MonitorType.HTTP,
        name="Website",
        url="https://website.com"
    )
