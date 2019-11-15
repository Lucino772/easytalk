import sys
from easytalk import Stream

# RECEIVE DATA
s = Stream.from_sys()
data = s.recv()  # do something with the data

# SEND DATA
s.send(b'Message from subprocess !')