import sys
import os.path as path
from subprocess import Popen, PIPE

from easytalk import Stream

# RUN THE SUBPROCESS
proc = Popen([sys.executable,path.join(path.dirname(__file__),'./proc.py')],stdin=PIPE,stdout=PIPE,stderr=sys.stdout)

s = Stream.from_subprocess(proc)

# SEND DATA
s.send(b'Message from main process !')
# RECEIVE DATA
data = s.recv()
print(data)

# WAIT FOR PROCESS TO CLOSE
proc.wait()