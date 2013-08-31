from timer import Timer
from redis import Redis
rdb = Redis()

with Timer() as t:
    rdb.lpush("foo", "bar")
print "=> elasped lpush: %s s" % t.secs

#with Timer() as t:
    #rdb.lpop("foo")

with Timer() as t:
    rdb.lpop("foo")
    for i in range(0,10000000, 1):
        a = 3


print "=> elasped lpop: %s s" % t.secs

