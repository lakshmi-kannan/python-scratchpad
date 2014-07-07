#!/usr/bin/env python2.7

from pytz import utc
import time

import eventlet
from apscheduler.schedulers.background import BackgroundScheduler


def test_aps_eventlet():
    def showMessage():
        print "Show this message"

    sh = BackgroundScheduler()
    sh.start()
    sh.add_job(showMessage, 'interval', seconds=2, timezone=utc)
    time.sleep(10)

if __name__ == '__main__':
    eventlet.monkey_patch(
        os=True,
        select=True,
        socket=True,
        thread=True,
        time=True)

    test_aps_eventlet()
