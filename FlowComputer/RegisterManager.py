import struct

class RegisterManager:
    def __init__(self, context):
        self.context = context

    def write_float(self, address: int, value: float):
        packed = struct.pack(">f", value)
        high_word, low_word = struct.unpack(">HH", packed)
        
        slave_store = self.context[1]
        slave_store.setValues(3, address, [high_word, low_word])