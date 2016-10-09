"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class crazyflie_pos_t(object):
    __slots__ = ["timestamp", "x", "y", "z", "roll", "pitch", "yaw"]

    def __init__(self):
        self.timestamp = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(crazyflie_pos_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qdddddd", self.timestamp, self.x, self.y, self.z, self.roll, self.pitch, self.yaw))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != crazyflie_pos_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return crazyflie_pos_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = crazyflie_pos_t()
        self.timestamp, self.x, self.y, self.z, self.roll, self.pitch, self.yaw = struct.unpack(">qdddddd", buf.read(56))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if crazyflie_pos_t in parents: return 0
        tmphash = (0x83f9d8d6ef5b5533) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if crazyflie_pos_t._packed_fingerprint is None:
            crazyflie_pos_t._packed_fingerprint = struct.pack(">Q", crazyflie_pos_t._get_hash_recursive([]))
        return crazyflie_pos_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

