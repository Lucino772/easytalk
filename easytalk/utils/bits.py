
def to_bits(_bytes: bytes) -> list:
    bits = []
    offset = 0
    for byte in _bytes:
        for i in range(8):
            bits.insert(0+offset,(byte >> i) & 1)
        offset += 8
    return bits

def from_bits(bits: list) -> bytes:
    if not len(bits) % 8 == 0:
        print('Invalid bits length !')
        return b''
    _bytes = b''
    offset = 0
    for i in range(0,int(len(bits) / 8)):
        byte = int(''.join(map(lambda x: str(x), bits[offset:offset+8])), 2).to_bytes(1, byteorder='little')
        _bytes += byte
        offset += 8
    return _bytes

def shuffle(bits: list) -> list:
    if not len(bits) % 8 == 0:
        print('Invalid bits length !')
        return []
    _bits = bits.copy()
    i = 0
    for bit in bits:
        if i % 2 == 0:
            _bits[i] = bits[i+1]
            _bits[i+1] = bits[i]
        i+=1
    return _bits

def as_string(bits: list) -> str:
    if not len(bits) % 8 == 0:
        print('Invalid bits length !')
        return ''
    parts = []
    offset = 0
    for i in range(0,int(len(bits) / 8)):
        _8bits = bits[offset:offset+8]
        parts.append(''.join(map(lambda x: str(x), _8bits)))
        offset += 8
    return ' '.join(map(lambda x: str(x), parts))
