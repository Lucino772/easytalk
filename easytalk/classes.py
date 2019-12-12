import io
import sys
import uuid
import time
import socket
import atexit

from threading import Thread
from subprocess import Popen

from easytalk import bits

class Buffer:
    
    def __init__(self,data=bytes()):
        """Initialize a buffer with some data"""
        self.data = data
    
    def to_stream(self,stream: io.BufferedWriter):
        """Send data from the buffer to a stream"""
        stream.write(len(self.data).to_bytes(4,'big'))
        stream.write(bits.encode(self.data))
        stream.flush()
    
    def from_stream(self,stream: io.BufferedReader):
        """Receive data from a stream into the buffer"""        
        size = int.from_bytes(stream.read(4),'big')
        self.data = bits.decode(stream.read(size))
        return self
    
    def clear(self):
        """Clear buffer"""
        self.data = bytes()

class Stream:

    @staticmethod
    def from_sock(sock: socket.socket):
        return Stream(sock.makefile('rb'),sock.makefile('wb'))

    @staticmethod
    def from_sys():
        return Stream(sys.stdin.buffer,sys.stdout.buffer)
    
    @staticmethod
    def from_subprocess(proc: Popen):
        use_buffer = getattr(proc.stdout,'buffer',None)
        if use_buffer:
            return Stream(proc.stdout.buffer,proc.stdin.buffer)
        return Stream(proc.stdout,proc.stdin)
            

    def __init__(self,_in: io.BufferedReader,_out: io.BufferedWriter):
        self.__in = _in
        self.__out = _out
    
    def send(self,data: bytes):
        Buffer(data).to_stream(self.__out)
    
    def recv(self):
        b = Buffer().from_stream(self.__in)
        return b.data
    
    def close(self):
        self.__in.close()
        self.__out.close()

class Item:

    def __init__(self,stream: Stream,autoclose=False):
        self.__stream = stream
        self.__id = str(uuid.uuid1())
        self.__messages = {}
        if autoclose:
            atexit.register(self.close)
    
    def get_id(self):
        return self.__id
    
    def send(self,data: bytes,response=False,timeout=5):
        msg_id = str(uuid.uuid1())
        # Create message
        _bytes = bytearray()
        _bytes.extend(msg_id.encode('utf-8'))
        _bytes.extend(data)
        _bytes = bytes(_bytes)
        # Register message
        if response:
            self.__messages[msg_id] = {'data': None}
        # Send message
        self.__stream.send(_bytes)
        # Wait for response
        if not response:
            return None
        start_time = time.time()
        while time.time() - start_time < 5:
            resp = self.__messages[msg_id]['data']
            if resp:
                self.__messages.pop(msg_id)
                return resp
        return None
    
    def listen(self,on_data=None,on_error=None):
        def listener():
            try:
                while True:
                    data = self.__stream.recv()
                    # Read message id
                    print(data)
                    if len(data) > 36:
                        msg_id = data[:36].decode('utf-8')
                        msg = data[36:]
                        if msg_id in self.__messages.keys():
                            self.__messages[msg_id] = {'data': msg}
                        elif callable(on_data):
                            resp = on_data(self.__id,msg)
                            _bytes = bytearray()
                            _bytes.extend(msg_id.encode('utf-8'))
                            _bytes.extend(resp)
                            _bytes = bytes(_bytes)
                            self.__stream.send(_bytes)
            finally:
                pass
#             except Exception as err:
#                 if callable(on_error):
#                     on_error(repr(err))
        th = Thread(target=listener,daemon=True)
        th.start()

    def close(self):
        self.__stream.close()

