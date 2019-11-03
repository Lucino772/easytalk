import io
import sys

import easytalk.utils.bits as bits

MSG_LEN_SIZE = 4
CHANNEL_ID_SIZE = 1

class Stream:

    @staticmethod
    def from_socket(sock):
        return Stream.get_pair(sock.makefile(mode='rb'),sock.makefile(mode='wb'))
    
    @staticmethod
    def from_sys():
        return Stream.get_pair(sys.stdin.buffer,sys.stdout.buffer)

    @staticmethod
    def get_pair(_in: io.BufferedIOBase,_out: io.BufferedIOBase):
        reader = Stream(_in)
        writer = Stream(_out)
        return reader, writer


    def __init__(self,buffer: io.BufferedIOBase):
        self.__buffer = buffer
    
    def send(self,data: bytes,channel_id=0):
        # WRITE LENGTH
        size_bytes = len(data).to_bytes(MSG_LEN_SIZE,'big')
        self.__buffer.write(size_bytes) 
        # WRITE CHANNEL
        self.__buffer.write(channel_id.to_bytes(CHANNEL_ID_SIZE,'big'))
        # ENCODE DATA
        encoded_data = bits.from_bits(bits.shuffle(bits.to_bits(data)))
        # WRITE DATA
        self.__buffer.write(encoded_data)
        # FLUSH STREAM
        self.__buffer.flush()
    
    def recv(self):
        # READ LENGTH
        size = int.from_bytes(self.__buffer.read(MSG_LEN_SIZE),byteorder='big')
        # READ CHANNEL ID
        channel_id = int.from_bytes(self.__buffer.read(CHANNEL_ID_SIZE),byteorder='big')
        # READ DATA
        data = self.__buffer.read(size)
        # DECODE DATA
        decoded_data = bits.from_bits(bits.shuffle(bits.to_bits(data)))
        # RETURN DATA
        return decoded_data, channel_id
