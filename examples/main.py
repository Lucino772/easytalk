import sys
import os.path as path

from subprocess import Popen, PIPE
from easytalk.classes.stream import Stream
from easytalk.classes.channel import Channels

proc = Popen([sys.executable,path.join(path.dirname(__file__),'./myproc.py')],stdin=PIPE,stdout=PIPE)

reader, writer = Stream.get_pair(proc.stdout,proc.stdin)

# RECEIVE DATA
data,_ = reader.recv()
print('Data received: {}'.format(data))

# RECEIVE DATA WITH CHANNEL_ID
data,channel_id = reader.recv()
print('Data received on channel {}: {}'.format(channel_id,data))
