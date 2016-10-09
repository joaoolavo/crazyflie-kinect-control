"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class crazyflie_input_t(object):
    __slots__ = ["timestamp", "input", "offset", "type"]

    def __init__(self):
        self.timestamp = 0
        self.input = [ 0.0 for dim0 in range(4) ]
        self.offset = 0.0
        self.type = ""

    def encode(self):
        buf = BytesIO()
        buf.write(crazyflie_input_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        buf.write(struct.pack('>4d', *self.input[:4]))
        buf.write(struct.pack(">d", self.offset))
        __type_encoded = self.type.encode('utf-8')
        buf.write(struct.pack('>I', len(__type_encoded)+1))
        buf.write(__type_encoded)
        buf.write(b"\0")

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != crazyflie_input_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return crazyflie_input_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = crazyflie_input_t()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        self.input = struct.unpack('>4d', buf.read(32))
        self.offset = struct.unpack(">d", buf.read(8))[0]
        __type_len = struct.unpack('>I', buf.read(4))[0]
        self.type = buf.read(__type_len)[:-1].decode('utf-8', 'replace')
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if crazyflie_input_t in parents: return 0
        tmphash = (0x856c925134afc6c8) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if crazyflie_input_t._packed_fingerprint is None:
            crazyflie_input_t._packed_fingerprint = struct.pack(">Q", crazyflie_input_t._get_hash_recursive([]))
        return crazyflie_input_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

