import gevent
import urllib2
from timbr.serializer import custom_encode

image_url = "http://manage.hdrelay.com/snapshot/ee489921-1004-45df-9634-0fa96543dabf?size=710x425&f=30000"
polling_interval = "31"

def stream():
    while True:
        msg = {"media_url": image_url}
        msg["polling_interval"] = float(polling_interval)
        msg["media"] = custom_encode(urllib2.urlopen(msg["media_url"]))
        yield msg
        gevent.sleep(float(polling_interval))
