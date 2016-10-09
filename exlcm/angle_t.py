"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class angle_t(object):
    __slots__ = ["timestamp", "roll", "pitch", "yaw", "enabled"]

    def __init__(self):
        self.timestamp = 0
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.enabled = False

    def encode(self):
        buf = BytesIO()
        buf.write(angle_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qdddb", self.timestamp, self.roll, self.pitch, self.yaw, self.enabled))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != angle_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return angle_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = angle_t()
        self.timestamp, self.roll, self.pitch, self.yaw = struct.unpack(">qddd", buf.read(32))
        self.enabled = bool(struct.unpack('b', buf.read(1))[0])
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if angle_t in parents: return 0
        tmphash = (0x1052689d368f1671) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if angle_t._packed_fingerprint is None:
            angle_t._packed_fingerprint = struct.pack(">Q", angle_t._get_hash_recursive([]))
        return angle_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

