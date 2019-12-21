import sys
import os.path as path
from subprocess import Popen, PIPE

from easytalk import Stream, Item

# Callback for incoming data
def on_data(msg_id: str,data: bytes,channel: int):
    print(msg_id,data,channel) # Do somthing with data

# Callback for error (normally means that the stream is closed)
def on_error(error):
    print('ERROR:',error)

# Run the subprocess
proc = Popen(
    [sys.executable,path.join(path.dirname(__file__),'./proc.py')],
    stdin=PIPE,
    stdout=PIPE,
    stderr=sys.stdout) # stderr: only for debugging

s = Stream.from_subprocess(proc) # Create a stream instance
i = Item(s) # Create an item instance
i.listen(on_data,on_error) # Start listening for data

# Send data and expect response
resp = i.send(b'Hello World !',response=True)
print(resp)

# Wait for process to close
proc.communicate()