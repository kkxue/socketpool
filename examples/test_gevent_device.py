# -*- coding: utf-8 -
#
# This file is part of socketpool.
# See the NOTICE for more information.

import gevent

from socketpool.pool import ConnectionPool
from socketpool.conn import DeviceConnector


if __name__ == '__main__':
    import time

    conInfo = "ssh#192.168.1.95#admin#Sdntiger"
    options = {'devType': 'huawei', 'connInfo': conInfo}
    pool = ConnectionPool(factory=DeviceConnector, backend="gevent", max_size=2)

    def runpool(data):
        with pool.connection(**options) as conn:
            print ("conn: pool size: %s" % pool.size)
            print conn


    start = time.time()
    jobs = [gevent.spawn(runpool, "blahblah") for _ in xrange(6)]

    gevent.joinall(jobs)
    delay = time.time() - start

    print ("final pool size: %s" % pool.size)
