import lcm

from exlcm import example_t

def my_handler(channel, data):
    msg = example_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   x   = %s" % str(msg.position[0]))
    print("   y   = %s" % str(msg.position[1]))
    print("   z   = %s" % str(msg.position[2]))
    print("")

lc = lcm.LCM()
subscription = lc.subscribe("POS_CF", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)
