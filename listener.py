import lcm

from exlcm import angle_t

def my_handler(channel, data):
    msg = angle_t.decode(data)
    #print("Received message on channel \"%s\"" % channel)
    print("   roll   = %s" % str(msg.roll))
    print("   pitch   = %s" % str(msg.pitch))
    print("   yaw   = %s" % str(msg.yaw))
    print("")

lc = lcm.LCM()
subscription = lc.subscribe("ANG_CF", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)
