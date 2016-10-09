import lcm
import time

from exlcm import angle_t

lc = lcm.LCM()

msg = angle_t()
msg.timestamp = 0
msg.roll = 0
msg.pitch = 1
msg.yaw = 2
msg.enabled = 1

lc.publish("ANG_CF", msg.encode())
